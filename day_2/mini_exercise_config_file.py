from loguru import logger
from pathlib import Path
import configparser

# Mini Exercise: Config File Handling
# With reference to the books config file, perform the following tasks:
# Given the information of what customers bought calculate the total sale
# of books made when books are purchased by  customer and log the output in a formatted manner
# Please be aware that some customers are regular buyers, some are members and
# some are premium members. The discount rates are as follows:
# Regular Buyers: 5% discount
# Members: 10% discount
# Premium Members: 15% discount
# You have to calculate the total sales made on a single day along with
# the breakdown of customer purchase total.

# Define the function to calculate total sales
def calculate_total_sales(config_file_path, total_purchases):
    """
    Calculate total sales based on book purchases and member discounts.
    
    Args:
        config_file_path: Path to the configuration file containing book prices
        total_purchases: Dictionary with customer purchase information
        
    Returns:
        Total sales amount after applying discounts and a dictionary containing
        customer purchase total
    """
    # Create a config parser object
    config = configparser.ConfigParser()

    # Read from the configuration file
    try:
        config.read(config_file_path)
    except configparser.Error as e:
        logger.error(f"Configuration file not found. Error: {e}")
        exit(1)

    # Define the total sales column
    total_sales = 0.0
    purchase_total = {} # Get the purchase total for every customer

    # Iterate through the total purchases dictionary
    for customer_id, customer_data in total_purchases.items():
        # Get the member info and purchase information from the nested dictionary
        member_type = customer_data.get('member_type', 'n')
        purchases = customer_data.get('purchases', [])

        # Initialise customer_subtotal
        customer_subtotal = 0.0

        for book_types in purchases:
            try:
                # Get price from the config file
                price = float(config.get('BOOK_COST', book_types))
                customer_subtotal += price
            except configparser.NoOptionError as e:
                logger.warning(f"Could not find the price for {book_types}")
                continue
        # Apply discounts
        discount_amount = customer_subtotal * float(config.get("DISCOUNTS", member_type))
        customer_total = customer_subtotal - discount_amount
        # Add the purchase subtotal for every customer
        purchase_total[customer_id] = purchase_total.get(customer_id, 0.0) + customer_total

        # Now add this subtotal to the final total to get the sale amount for the day
        total_sales += customer_total

    return total_sales, purchase_total
            

# Define the config file path
config_file_path = Path(__file__).parent / "configs" / "config_file_books.ini"

# Initialise the total purchases dictionary where the key is the customer_id
# value is a nested dictionary where in the member_type and purchases are listed
total_purchases = {
    1: {
        "member_type": 'r', # Regular
        "purchases": ['Fiction', 'Non-Fiction', 'Science']
    },
    2: {
        "member_type": 'p', # Premium member
        "purchases": ['Non-Fiction', 'Science']
    },
    3: {
        "member_type": 'n', # new
        "purchases": ['Science']
    },
    4: {
        "member_type": 'm', # Member
        "purchases": ['Fiction', 'Non-Fiction', 'Science', 'Children']
    }
}

total_sales, purchase_total = calculate_total_sales(config_file_path, total_purchases)
logger.info(f"Total sale for the day is: {total_sales}")
logger.info(f"Breakdown of Customer total: {purchase_total}")