class Bank:
    def __init__(self):
        self.accounts = {}
        self.loan_feature_enabled = True  # Initialize the loan feature as enabled

    # ...

    def toggle_loan_feature(self):
        self.loan_feature_enabled = not self.loan_feature_enabled

    # Add a method to check if the loan feature is enabled
    def is_loan_feature_enabled(self):
        return self.loan_feature_enabled
