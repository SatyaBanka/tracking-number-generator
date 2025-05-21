import hashlib
import string
import random
from datetime import datetime
from uuid import UUID

def generate_tracking_number(
    origin_country_id,
    destination_country_id,
    weight,
    created_at,
    customer_id,
    customer_name,
    customer_slug
):
    # Normalize and sanitize inputs
    origin = origin_country_id.upper()
    destination = destination_country_id.upper()
    weight_str = f"{float(weight):.3f}".replace('.', '')[:5]  # 1.234 → "1234"
    
    try:
        # Validate and normalize UUID
        customer_id_str = UUID(customer_id).hex.upper()[:6]
    except ValueError:
        customer_id_str = ''.join(random.choices(string.ascii_uppercase + string.digits, k=6))

    # Use initials of customer name
    customer_initials = ''.join([c for c in customer_name.upper() if c.isalnum()])[:3]
    
    # Slug - just letters and numbers
    slug_part = ''.join(filter(str.isalnum, customer_slug.upper()))[:3]

    # Normalize timestamp
    try:
        timestamp = datetime.fromisoformat(created_at).strftime('%Y%m%d%H%M%S')
    except Exception:
        timestamp = datetime.utcnow().strftime('%Y%m%d%H%M%S')

    # Compose base string to hash
    base = f"{origin}{destination}{weight_str}{customer_id_str}{customer_initials}{slug_part}{timestamp}"

    # Hash for uniqueness and shorten
    hash_part = hashlib.sha256(base.encode()).hexdigest().upper()[:6]

    # Combine and trim to 16 characters max
    tracking_number = f"{origin}{destination}{slug_part}{hash_part}"[:16]

    return tracking_number
