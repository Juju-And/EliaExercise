"""
In this assignment you should be able to extract the sentences from provided
samples on Amazon website.
You will only work with 'customer_reviews' column and first 1000 rows.
The customer reviews should be cleaned from html and segmented into sentences.
The result sentences should be saved in the file named cleaned_customer_reviews.txt,
separated by one blank line by keeping the same order.
"""
import pandas as pd


def clean_sentence():
    df = pd.read_csv(
        "amazon_co-ecommerce_sample.csv", usecols=["customer_reviews",], nrows=1000
    )

    reviews = df.customer_reviews.str.split(r"\s+\n\s+.+\s*\n\s+\n").explode(
        ignore_index=True
    )
    f = reviews.str.split(r"(\n|\/\/)").explode().to_frame()

    f["count"] = f.customer_reviews.str.count(r"\w+").to_frame()

    f.reset_index(level=0, inplace=True)

    max_idx = f.groupby(["index"], sort=False, dropna=False)["count"].idxmax()

    f["old_idx"] = f.index
    mw = f[f["old_idx"].isin(max_idx)]
    result = mw[~mw["customer_reviews"].str.match(r".*\d\d\d\d")]
    result["customer_reviews"].to_csv(
        "cleaned_customer_reviews.txt", header=False, index=False
    )


if __name__ == "__main__":
    clean_sentence()
