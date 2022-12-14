% of All Baked = 
VAR ALLBaked =
CALCULATE(
    [Total Baked],
    REMOVEFILTERS(
        'Food Inventory'
    )
)
VAR Ratio =
DIVIDE(
    [Total Baked],
    ALLBaked,
    "0"
)
RETURN
Ratio


% of Store-Level Sales = 
VAR StoreLevelSales = 
CALCULATE(
    [Customer Sales],
    REMOVEFILTERS(
        'Customer Lookup'
    ),
    KEEPFILTERS(
        'Calendar'
    )
)
VAR Ratio = 
DIVIDE(
    [Customer Sales (ALLEXCEPT Assignment)],
    StoreLevelSales
)
RETURN
Ratio


% of Total Baked (ALLSELECTED) = 
VAR SelectedQuantityBaked = 
CALCULATE(
    [Total Baked],
    ALLSELECTED(
    )
)
VAR Ratio = 
DIVIDE(
    [Total Baked],
    SelectedQuantityBaked,
    "0"
)
RETURN
Ratio


% of Total Sold (ALLSELECTED) = 
VAR SelectedQuantitySold = 
CALCULATE(
    [Total Sold],
    ALLSELECTED(
    )
)
VAR Ratio = 
DIVIDE(
    [Total Sold],
    SelectedQuantitySold,
    "0"
)
RETURN
Ratio


Count of Product ID (DISTINCT) = 
COUNTROWS(
    DISTINCT(
        'Product Lookup'[product_id]
    )
)


Count of Product ID (VALUES) = 
COUNTROWS(
    VALUES(
        'Product Lookup'[product_id]
    )
)


Customer Sales (ALLEXCEPT Assignment) = 
CALCULATE(
    [Customer Sales],
    ALLEXCEPT(
        'Sales by Store',
        'Calendar'[Transaction_Date],
        'Store Lookup'[store_id],
        'Customer Lookup'[customer_first-name],
        'Product Lookup'[product_group]
    )
)

Customer Sales (ALLEXCEPT) = 
CALCULATE(
    [Customer Sales],
    ALLEXCEPT(
        'Sales by Store',
        'Product Lookup'[product_group],
        'Calendar'[Transaction_Date]
    )
)

Customer Sales (ALLSELECTED) = 
CALCULATE(
    [Customer Sales],
    ALLSELECTED(
    )
)


Food Sold (SUMMARIZE Table) = 
SUM(
    'Unsold Pastries'[quantity_sold]
)

Food Unsold (SUMMARIZE Table) = 
SUMX(
    'Unsold Pastries',
    'Unsold Pastries'[quantity_start_of_day] - 'Unsold Pastries'[quantity_sold]
)

Lost Revenue (SUMMARIZE Table) = 
SUMX(
    'Unsold Pastries',
    [Food Unsold (SUMMARIZE Table)] *'Unsold Pastries'[current_retail_price]
)

Quantity Sold (SELECTEDVALUE) = 
DIVIDE(
    [Customer Sales],
    SELECTEDVALUE(
        'Product Lookup'[current_retail_price]
    )
)

Retail Price (SELECTEDVALUE) = 
SELECTEDVALUE(
    'Product Lookup'[current_retail_price]
)

Total Baked = 
SUMX(
    'Food Inventory',
    'Food Inventory'[quantity_start_of_day]
)

Total Sold = 
SUMX(
    'Food Inventory',
    'Food Inventory'[quantity_sold]
)
