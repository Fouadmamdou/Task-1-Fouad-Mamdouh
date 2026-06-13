import pandas as pd
import numpy as np

INPUT_FILE = "Dataset for Data Analytics.xlsx"
OUTPUT_FILE = "Dataset_Cleaned.xlsx"

df = pd.read_excel(INPUT_FILE)

print(f"Original shape: {df.shape}")

# ── 1. Fill CouponCode nulls 
df["CouponCode"] = df["CouponCode"].fillna("No Coupon")

# ── 2. Rename ItemsInCart → CartSize
df = df.rename(columns={"ItemsInCart": "CartSize"})

# ── 3. Flag ShippingAddress as incomplete
# All addresses are "XXX Main St" with no city/state/ZIP — unusable for geo analysis.
# We add a boolean flag column to mark them and keep the original for reference.
df["ShippingAddress_Complete"] = False

# ── 4. Nullify TrackingNumber for Pending and Cancelled orders
df.loc[df["OrderStatus"].isin(["Pending", "Cancelled"]), "TrackingNumber"] = np.nan

# ── Verification ──────────────────────────────────────────────────────────────
print("\n── Cleaning results ──")
print(f"CouponCode nulls remaining : {df['CouponCode'].isnull().sum()}")
print(f"CouponCode unique values   : {sorted(df['CouponCode'].unique())}")
print(f"Column 'CartSize' exists   : {'CartSize' in df.columns}")
print(f"ShippingAddress_Complete   : {df['ShippingAddress_Complete'].unique()}")

tracking_check = df.groupby("OrderStatus")["TrackingNumber"].apply(
    lambda x: x.isnull().sum()
)
print(f"\nNull TrackingNumbers by status:\n{tracking_check}")

print(f"\nCleaned shape: {df.shape}")

# ── Save ──────────────────────────────────────────────────────────────────────
df.to_excel(OUTPUT_FILE, index=False)
print(f"\nSaved → {OUTPUT_FILE}")
