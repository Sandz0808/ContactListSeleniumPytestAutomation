from faker import Faker


class DataGenerator:
    def __init__(self):
        self.fake = Faker()

    def generate_valid_signup_data(self):
        """Generate valid signup data."""
        return {
            "firstName": self.fake.first_name(),
            "lastName": self.fake.last_name(),
            "email": self.fake.unique.email(),
            "password": self.fake.password(length=8)
        }

    def generate_invalid_signup_data(self):
        """Generate invalid signup data."""
        return {
            "firstName": self.fake.first_name(),
            "lastName": self.fake.last_name(),
            "email": "invalid-email",
            "password": "1234567",
            "result":"User validation failed: email: Email is invalid"
        }

    def generate_valid_add_contact_data(self):
        """Generate contact data with an option to create valid or invalid signup data."""

        return {
            "firstName": self.fake.first_name(),
            "lastName": self.fake.last_name(),
            "birthdate": self.fake.date_of_birth(minimum_age=18, maximum_age=60).strftime("%Y-%m-%d"),
            "email": self.fake.email(),
            "phone": self.fake.random_number(digits=10, fix_len=True),
            "street1": self.fake.street_address(),
            "street2": self.fake.secondary_address(),
            "city": self.fake.city(),
            "stateProvince": self.fake.state(),
            "postalCode": self.fake.postcode(),
            "country": self.fake.country(),
            }


    def generate_invalid_add_contact_data(self):
        """Generate contact data with an option to create valid or invalid signup data."""

        return {
            "firstName": "",
            "lastName": self.fake.last_name(),
            "birthdate": self.fake.date_of_birth(minimum_age=18, maximum_age=60).strftime("%Y-%m-%d"),
            "email": self.fake.email(),
            "phone": self.fake.random_number(digits=10, fix_len=True),
            "street1": self.fake.street_address(),
            "street2": self.fake.secondary_address(),
            "city": self.fake.city(),
            "stateProvince": self.fake.state(),
            "postalCode": self.fake.postcode(),
            "country": self.fake.country(),
            }
