import pandas as pd


def load_data(path: str):
    df = pd.read_csv(path)

    print(f"Shape: {df.shape}")
    print(df["Class"].value_counts())

    return df


if __name__ == "__main__":
    df = load_data("data/creditcard.csv")