import pyfiglet
import phonenumbers
from phonenumbers import timezone, geocoder, carrier, number_type, format_number, PhoneNumberFormat
import datetime
import pytz

ascii_banner = pyfiglet.figlet_format("Phone Lookup - Made By Exploits")
print(ascii_banner)

def is_valid_phone_number(number):
    """Check if the phone number is valid and return a tuple of (is_valid, message)."""
    try:
        phone = phonenumbers.parse(number)
        if not phonenumbers.is_valid_number(phone):
            return (False, "The phone number is not valid. Please make sure it's in the correct format (e.g., +11234567890).")
        return (True, phone)
    except phonenumbers.phonenumberutil.NumberParseException:
        return (False, "The phone number entered is not valid. Please make sure it's in the correct format (e.g., +14155552671).")

number = input("Enter your number here (e.g., +11234567890): ")

validity, result = is_valid_phone_number(number)

current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

if not validity:
    print(result)  
else:
    phone = result 

    time_zone = timezone.time_zones_for_number(phone)
    carrier_name = carrier.name_for_number(phone, "en") if carrier.name_for_number(phone, "en") else "Unknown Carrier"
    region = geocoder.description_for_number(phone, "en")

    country_code = phone.country_code
    national_number = phone.national_number
    
    region_code = phonenumbers.region_code_for_number(phone)
    country_name = geocoder.country_name_for_number(phone, "en") 

    phone_type = number_type(phone)

    if phone_type == phonenumbers.PhoneNumberType.MOBILE:
        phone_type_str = "Mobile - A mobile phone number."
    elif phone_type == phonenumbers.PhoneNumberType.FIXED_LINE:
        phone_type_str = "Fixed Line - A landline number."
    elif phone_type == phonenumbers.PhoneNumberType.FIXED_LINE_OR_MOBILE:
        phone_type_str = "Fixed Line or Mobile - Could be either."
    elif phone_type == phonenumbers.PhoneNumberType.VOIP:
        phone_type_str = "VoIP - Voice over IP number, such as Skype."
    else:
        phone_type_str = "Unknown - Type could not be determined."

    formatted_number = format_number(phone, PhoneNumberFormat.INTERNATIONAL)
    formatted_number_national = format_number(phone, PhoneNumberFormat.NATIONAL)
    formatted_number_e164 = format_number(phone, PhoneNumberFormat.E164)

print("\n--- Phone Number Information ---")
print(f"✔️ Valid Number: {validity}")
print(f"🌍 Formatted Phone Number (International): {formatted_number}")
print(f"🗺️ Formatted Phone Number (National): {formatted_number_national}")
print(f"📱 Formatted Phone Number (E.164): {formatted_number_e164}")
print(f"🌐 Country Code: {country_code}") 
print(f"📡 Carrier: {carrier_name}")

if time_zone:
    for tz in time_zone:
        timezone_obj = pytz.timezone(tz)
        timezone_time = datetime.datetime.now(timezone_obj).strftime("%Y-%m-%d %H:%M:%S")
        print(f"🕒 Current Date and Time in {tz}: {timezone_time}")
else:
    print("🌍 Time Zone: Unknown Time Zone")

print(f"🌎 Country Name: {country_name if country_name else 'Unknown Country'}")
print(f"🏙️ Region: {region if region else 'Unknown Region'}")
print(f"📞 Phone Type: {phone_type_str}")
print("\n--- End of Information ---")