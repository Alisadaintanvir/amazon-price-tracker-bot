from price_tracker import PriceTracker
from notification import Notification
from dotenv import load_dotenv

load_dotenv()


PRODUCT_URL = "https://www.amazon.com/dp/B075CYMYK6?ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6&th=1"
price_tracker = PriceTracker(PRODUCT_URL)

current_price = price_tracker.request()
target_price = 70

notification = Notification(price_tracker.title, current_price, PRODUCT_URL)
if current_price <= target_price:
    notification.send_notification()

