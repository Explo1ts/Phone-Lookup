# Phone-Lookup - Made By Exploits

Overview
The Phone Lookup tool is a Python application that utilizes the phonenumbers library to validate and provide detailed information about a given phone number. This tool allows users to check the validity of a phone number, retrieve its geographic and carrier information, and format the number in various ways.

Features
1. Phone Number Validation
Check Validity: The application checks if the entered phone number is valid, ensuring it is in the correct international format (e.g., +11234567890).
Error Handling: Provides user-friendly error messages if the number is not valid, clearly indicating the issue.
2. Detailed Phone Information
If the phone number is valid, the tool retrieves various pieces of information such as:

Formatted Numbers: Displays the phone number in multiple formats:

International Format: Standard international dialing format.
National Format: Standard format for local dialing.
E.164 Format: Standardized format for international telecommunication.
Country Code: Indicates the country code of the phone number.

Carrier Information: Displays the carrier associated with the phone number.

Geographic Information:

Country Name: The name of the country where the phone number is registered.
Region: The specific region within the country associated with the phone number.
3. Time Zone Information
Current Date and Time: The application provides the current date and time in the time zone corresponding to the phone number, helping users understand local time.
4. Phone Type Identification
Identifies the type of phone number, differentiating between mobile, fixed-line, VoIP, and unknown phone types. This can be useful for understanding the nature of the communication channel.
How to Use
Ensure you have Python installed along with the required libraries (phonenumbers, pyfiglet, and pytz).
Run the script.
When prompted, enter the phone number in international format (e.g., +11234567890).
The application will provide a comprehensive overview of the phone number, including validity, formatting, carrier, geographic region, and more.
