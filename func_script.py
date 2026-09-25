"""Small helper functions for cleaning currency-formatted columns."""


def char_del(df, columns, chars):
    """Remove each character in `chars` from the given `columns` of `df`, in place."""
    for col in columns:
        for ch in chars:
            df[col] = df[col].str.replace(ch, '', regex=False)
    return df


def col_div(df, column, divisor):
    """Cast `column` to int64 and divide by `divisor`, in place."""
    df[column] = df[column].astype('int64') / divisor
    return df
