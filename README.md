# Task-1
#Data cleaing & prepairing
Here's a summary of what this dataset is and what needs cleaning:
What it is: An e-commerce orders dataset with 1,200 transactions spanning January 2023 to June 2025. It covers 7 product types (Laptop, Phone, Tablet, Monitor, Chair, Printer, Desk), 5 payment methods, and 5 order statuses. It's clearly built for practicing sales/marketing analytics.
The 4 things cleaned:

1- CouponCode nulls (309 rows) — 26% of orders have no coupon, but the field is blank instead of labeled. Fill with "No Coupon" so filters and groupbys work properly.ItemsInCart vs Quantity mismatch (1,000 rows) 
2— ItemsInCart is always larger than Quantity, and pricing only aligns with Quantity. These two columns represent different things: how many units were ordered vs. how many were in the cart total. Rename ItemsInCart to CartSize to avoid confusion.
3- ShippingAddress is too thin, every address is just "XXX Main St" with no city, state, or ZIP. You can't do any geographic analysis with it. Either flag it as unusable or drop the column.
4- TrackingNumbers on Cancelled/Pending orders, every single order has a tracking number, even ones that were never shipped. That's likely placeholder data. Set tracking to null or "N/A" for orders with Pending or Cancelled status.
