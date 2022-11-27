import sys

header = open('../web/src/header.html', 'r').read()

sys.path.append('../cherrypy/')
import cherrypy

DB_STRING = 'chat_data.db'

# -*- coding: utf-8 -*-
import time
import sqlite3
import argparse
import random
import os

from ws4py.server.cherrypyserver import WebSocketPlugin, WebSocketTool
from ws4py.websocket import WebSocket
from ws4py.messaging import TextMessage

USERS = ['mike', 'stella', 'john']

DB_STRING = 'chat_data.db'

class ChatPlugin(WebSocketPlugin):
    def __init__(self, bus):
        WebSocketPlugin.__init__(self, bus)
        self.clients = {}

    def start(self):
        WebSocketPlugin.start(self)
        self.bus.subscribe('add-client', self.add_client)
        self.bus.subscribe('get-client', self.get_client)
        self.bus.subscribe('del-client', self.del_client)

    def stop(self):
        WebSocketPlugin.stop(self)
        self.bus.unsubscribe('add-client', self.add_client)
        self.bus.unsubscribe('get-client', self.get_client)
        self.bus.unsubscribe('del-client', self.del_client)

    def add_client(self, name, websocket):
        self.clients[name] = websocket

    def get_client(self, name):
        return self.clients[name]

    def del_client(self, name):
        del self.clients[name]

class ChatWebSocketHandler(WebSocket):
    def opened(self):
        cherrypy.engine.publish('add-client', self.username, self)

    def received_message(self, m):
        text = m.data.decode('utf8')
        if text.find("@") == -1:
            # echo to all
            cherrypy.engine.publish('websocket-broadcast', m)
            timestamp = int(time.time())
            with sqlite3.connect(DB_STRING) as dbc:
                dbc.execute("INSERT INTO messages (username, message, created) VALUES (?, ?, ?)",
                            [self.username, text, timestamp])
        else:
            # or echo to a single user
            left, message = text.rsplit(':', 1)
            print(left)
            from_username, to_username = left.split('@')
            print(repr(from_username), repr(to_username), repr(self.username))
            client = cherrypy.engine.publish('get-client', to_username.strip()).pop()
            print(client)
            client.send("@@%s: %s" % (from_username.strip()[:-1], message.strip()))

    def closed(self, code, reason="A client left the room without a proper explanation."):
        cherrypy.engine.publish('del-client', self.username)
        cherrypy.engine.publish('websocket-broadcast', TextMessage(reason))

class Chat(object):
    def __init__(self, host, port, ssl=False, ssl_port=9443):
        self.host = host
        self.port = port
        self.ssl_port = ssl_port
        self.ssl = ssl
        self.scheme = 'wss' if ssl else 'ws'

    @cherrypy.expose
    def index(self):
        return header + """
    <h1>Data Tools Chat</h1>
    <form action='/chatroom' id='chatform' method='get'>
      <input type='text' name='username' id='username' class='form-control' placeholder="Digite seu nome de usuário"/><br />
      <input id='send' type='submit' value='Ir para o chat' class='form-control btn btn-primary'/>
      </form>
    </body>
    </html>
    """

    @cherrypy.expose
    def chatroom(self, username=None):
        username = username or "User%d" % random.randint(0, 100)
        messages = []
        with sqlite3.connect(DB_STRING) as dbc:
            result = dbc.execute("SELECT * FROM messages LIMIT 1000")
            for row in result:
                msg = row[2]
                messages.append(msg)

        return header + """<script   src="https://code.jquery.com/jquery-1.12.4.min.js"   integrity="sha256-ZosEbRLbNQzLpnKIkEdrPv7lOy9C27hHQ+Xp8a4MxAQ="   crossorigin="anonymous"></script>
      <script type='application/javascript'>
        $(document).ready(function() {
        
          websocket = '%(scheme)s://'+window.location.href.split("/")[2].replace(":9000","")+':%(port)s/ws?username=%(username)s';
          if (window.WebSocket) {
            ws = new WebSocket(websocket, ['tcp']);
          }
          else if (window.MozWebSocket) {
            ws = MozWebSocket(websocket);
          }
          else {
            console.log('WebSocket Not Supported');
            return;
          }
          window.onbeforeunload = function(e) {
            $('#chat').val($('#chat').val() + 'Bye bye...\\n');
            ws.close(1000, '**%(username)s**: Saiu da sala');
            if(!e) e = window.event;
            e.stopPropagation();
            e.preventDefault();
          };
          ws.onmessage = function (evt) {
             $('#chat').val($('#chat').val() + evt.data + '\\n');
             var textarea = document.getElementById('chat');
             textarea.scrollTop = textarea.scrollHeight;
          };
          ws.onopen = function() {
             ws.send("**%(username)s**: Entrou na sala");
          };
          ws.onclose = function(evt) {
             $('#chat').val($('#chat').val() + 'Connection closed by server: ' + evt.code + ' \"' + evt.reason + '\". Refresh to reconnect.\\n');
          };
          $('#send').click(function() {
             console.log($('#message').val());
             ws.send('**%(username)s**: ' + $('#message').val());
             $('#message').val("");
             return false;
          });
          var textarea = document.getElementById('chat');
          textarea.scrollTop = textarea.scrollHeight;
        });
      </script>
    <h1>Data Tools Chat</h1>
    <div  class="form-group">
        <form action='#' id='chatform' method='get'>
          <textarea id='chat' cols='35' rows='10' class="form-control"  disabled>%(messages)s</textarea>
          <br />
          <input type='text' id='message' class="form-control" placeholder='Digite sua mensagem' />
          <input id='send' type='submit' class="form-control"  value='Enviar mensagem' class='form-control btn btn-primary'/>
          </form>
    </div>
    </body>
    </html>
    """ % {'username': username, 
           'port': self.ssl_port if self.ssl else self.port, 'scheme': self.scheme,
           'messages': "\n".join(messages) +  "\n"}

    @cherrypy.expose
    def ws(self, username):
        # let's track the username we chose
        cherrypy.request.ws_handler.username = username
        cherrypy.log("Handler created: %s" % repr(cherrypy.request.ws_handler))

if __name__ == '__main__':
    import logging
    from ws4py import configure_logger
    configure_logger(level=logging.DEBUG)

    parser = argparse.ArgumentParser(description='Echo CherryPy Server')
    parser.add_argument('--host', default='127.0.0.1')
    #parser.add_argument('--host', default='0.0.0.0')
    parser.add_argument('-p', '--port', default=9000, type=int)
    parser.add_argument('--ssl-port', default=9443, type=int)
    parser.add_argument('--ssl', action='store_true')
    parser.add_argument('--cert', default='./server.crt', type=str)
    parser.add_argument('--key', default='./server.key', type=str)
    parser.add_argument('--chain', default='./server.chain', type=str)
    args = parser.parse_args()

    cherrypy.config.update({
        'server.socket_host': args.host,
        'server.socket_port': args.port,
        'tools.staticdir.root': os.path.abspath(os.path.join(os.path.dirname(__file__), 'static')),
    })
    config = {
        '/ws': {
            'tools.websocket.on': True,
            'tools.websocket.handler_cls': ChatWebSocketHandler,
            'tools.websocket.protocols': ['tcp', 'toto', 'mytest', 'hithere']
        },
        '/static': {
              'tools.staticdir.on': True,
              'tools.staticdir.dir': ''
        },
    }

    if args.ssl:
        ssl_server = cherrypy._cpserver.Server()
        ssl_server.socket_host = args.host
        ssl_server.ssl_certificate = args.cert
        ssl_server.ssl_private_key = args.key
        ssl_server.socket_port = args.ssl_port
        ssl_server.ssl_certificate_chain = args.chain
        ssl_server.subscribe()

    ChatPlugin(cherrypy.engine).subscribe()
    cherrypy.tools.websocket = WebSocketTool()

    app_root = Chat(args.host, args.port, args.ssl, ssl_port=args.ssl_port)
    cherrypy.quickstart(app_root, '/', config=config)
