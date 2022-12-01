

class TransformNumbers:
    """
    A class to transform numbers

    ---

    Attributes
    ----------
    df : DataFrame
        dataframe that contains numbers

    field : string
        The field name to clean and transform in number

    xlabel : string
    ylabel : string
        In case of graph situation, you can try to transform both axis


    Methods
    -------

    """

    def try_convert_generical_text_in_number_by_one_field(df, field):
        for i in range(0, len(df)):
            try:
                df[field][i] = float(str(df[field][i]).replace(f"\xa0", "").replace(" ", "").replace(",", "."))
            except:
                pass
        return df

    def convert_generical_text_in_number_by_fields(df, fields : list):
        for field in fields:
            df[field] = TransformNumbers.try_convert_generical_text_in_number_by_one_field(df, field)[field]
        return df

    def convert_generical_text_in_number(df):
        return TransformNumbers.convert_generical_text_in_number_by_fields(df, df.columns)