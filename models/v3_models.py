from django.db import models
from django.contrib import admin

# from v2.views import portfolio

class User(models.Model):
    id = models.AutoField(primary_key=True)
    uid = models.CharField(max_length=64, unique=True)
    tvid = models.CharField(max_length=128, unique=True)
    title = models.CharField(max_length=8, null=True, blank=True, default=None)
    first_name = models.CharField(max_length=32)
    last_name = models.CharField(max_length=32)
    national_id = models.CharField(max_length=16, null=True, blank=True, default=None)
    dob = models.DateField(null=True, blank=True, default=None)
    age = models.IntegerField(null=True, blank=True, default=0)
    email = models.CharField(max_length=64)
    password = models.CharField(max_length=128)
    mobile_number = models.CharField(max_length=16) # To-Do: changed from mobile_phone
    status = models.CharField(max_length=16)
    token = models.CharField(max_length=256, null=True, blank=True, default=None)
    otp_token = models.CharField(max_length=8, null=True, blank=True, default='')
    service_agreement_at = models.DateTimeField(null=True, blank=True, default=None)
    latest_service_agreement_version = models.CharField(max_length=16, null=True, blank=True, default=None) # To-Do: implement
    latest_service_agreement_at = models.DateTimeField(null=True, blank=True, default=None) # To-Do: implement

    current_mobile_state = models.CharField(max_length=64, null=True, blank=True, default=None) # To-Do: changed from current_active_screen
    default_mobile_screen = models.CharField(max_length=64, null=True, blank=True, default=None) # To-Do: changed from mobile_default_screen
    fcm_token = models.TextField(null=True, blank=True, default=None)

    verified_email = models.CharField(max_length=8, default='No')
    verified_email_at = models.DateTimeField(null=True, blank=True, default=None) # To-Do: implement
    verified_mobile_number = models.CharField(max_length=8, default='No') # To-Do: changed from verified_mobile_phone
    verified_mobile_number_at = models.DateTimeField(null=True, blank=True, default=None) # To-Do: implement

    kyc_terms_accepted_at = models.DateTimeField(null=True, blank=True, default=None) # To-Do: changed from kyc_accepted_at
    kyc_selfie_attempt = models.IntegerField(null=True, blank=True, default=0) # To-Do: changed from selfie_attempt
    kyc_reset_attempt = models.IntegerField(null=True, blank=True, default=0)
    kyc_confidence_logs = models.TextField(null=True, blank=True, default=None)
    verified_ndid = models.CharField(max_length=4, null=True, blank=True, default='No')
    verified_kyc = models.CharField(max_length=4, default='No')

    kyc_approved_counter = models.IntegerField(null=True, blank=True, default=0)
    kyc_approved_by = models.CharField(max_length=256, null=True, blank=True, default=None)
    kyc_rejected_counter = models.IntegerField(null=True, blank=True, default=0)
    kyc_rejected_by = models.CharField(max_length=256, null=True, blank=True, default=None)
    kyc_approved_at = models.DateTimeField(null=True, blank=True, default=None)
    kyc_rejected_at = models.DateTimeField(null=True, blank=True, default=None) # To-Do: implement
    on_chain_at = models.DateTimeField(null=True, blank=True, default=None) # To-Do: implement
    
    p2p_account_requested_at = models.DateTimeField(null=True, blank=True, default=None) # To-Do: implement
    p2p_account_connected = models.CharField(max_length=16, null=True, blank=True, default='No')
    p2p_account_connected_at = models.DateTimeField(null=True, blank=True, default=None)
    p2p_access_token = models.CharField(max_length=256, null=True, blank=True, default=None) # To-Do: changed from p2p_code
    
    role = models.CharField(max_length=16, null=True, blank=True, default=None)
    role_agreement_at = models.DateTimeField(null=True, blank=True, default=None)
    latest_role_agreement_at = models.DateTimeField(null=True, blank=True, default=None) # To-Do: implement
    
    flag_kind = models.CharField(max_length=16, null=True, blank=True, default=None)
    flag_sale = models.CharField(max_length=64, null=True, blank=True, default=None)

    onboarded_platform = models.CharField(max_length=16, null=True, blank=True, default=None) # To-Do: changed from onboard
    created_at = models.DateTimeField(auto_now_add=True, auto_now=False)
    activated_at = models.DateTimeField(null=True, blank=True, default=None)
    updated_at = models.DateTimeField(null=True, blank=True, default=None)
    terminated_at = models.DateTimeField(null=True, blank=True, default=None)
    logs = models.TextField(null=True, blank=True, default=None)

    def __str__(self):
        return str(self.first_name) + ' '  + str(self.last_name) + ' (' + str(self.email) + ')'

class UserAdmin(admin.ModelAdmin):
    search_fields=['tvid', 'uid', 'first_name', 'last_name', 'email', 'mobile_number', 'national_id', 'role']

class UserManifest(models.Model): # To-Do: changed from Manifest
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    first_name_en = models.CharField(max_length=32, null=True, blank=True, default=None) # To-Do: implement
    last_name_en = models.CharField(max_length=32, null=True, blank=True, default=None) # To-Do: implement
    marital_status = models.CharField(max_length=32, null=True, blank=True, default=None) # To-Do: changed from status
    card_expire = models.CharField(max_length=16, null=True, blank=True, default=None)
    card_image = models.CharField(max_length=64, null=True, blank=True, default=None)
    card_image_uploaded_at = models.DateTimeField(null=True, blank=True, default=None) # To-Do: implement
    face_image = models.CharField(max_length=64, null=True, blank=True, default=None)
    face_image_uploaded_at = models.DateTimeField(null=True, blank=True, default=None) # To-Do: implement
    
    kairos_enroll = models.TextField(null=True, blank=True, default=None)
    kairos_confidence = models.FloatField(null=True, blank=True, default=0)
    kairos_liveness = models.FloatField(null=True, blank=True, default=0) 
    kairos_verify = models.TextField(null=True, blank=True, default=None) 
    kairos_verified_at = models.DateTimeField(null=True, blank=True, default=None) # To-Do: implement
    
    ekyc_channel = models.CharField(max_length=16, null=True, blank=True, default=None)
    ndid_info_th = models.TextField(null=True, blank=True, default=None)
    ndid_info_en = models.TextField(null=True, blank=True, default=None)
    ndid_identifier = models.TextField(null=True, blank=True, default=None)
    ndid_dob = models.CharField(max_length=16, null=True, blank=True, default=None)
    ndid_address_primary = models.TextField(null=True, blank=True, default=None)
    ndid_address_secondary = models.TextField(null=True, blank=True, default=None)
    ndid_metadata = models.TextField(null=True, blank=True, default=None) # To-Do: changed from ndid_meta
    ndid_biometric = models.TextField(null=True, blank=True, default=None)
    ndid_verified_at = models.DateTimeField(null=True, blank=True, default=None) # To-Do: implement

    address = models.CharField(max_length=128, null=True, blank=True, default=None)
    street = models.CharField(max_length=64, null=True, blank=True, default=None)
    subdistrict = models.CharField(max_length=64, null=True, blank=True, default=None)
    district = models.CharField(max_length=64, null=True, blank=True, default=None)
    province = models.CharField(max_length=64, null=True, blank=True, default=None)
    postal_code = models.CharField(max_length=8, null=True, blank=True, default=None)
    use_primary_address = models.CharField(max_length=4, null=True, blank=True, default='Yes')
    address_2nd = models.CharField(max_length=128, null=True, blank=True, default=None)
    street_2nd = models.CharField(max_length=64, null=True, blank=True, default=None)
    subdistrict_2nd = models.CharField(max_length=64, null=True, blank=True, default=None)
    district_2nd = models.CharField(max_length=64, null=True, blank=True, default=None)
    province_2nd = models.CharField(max_length=64, null=True, blank=True, default=None)
    postal_code_2nd = models.CharField(max_length=8, null=True, blank=True, default=None)

    ncb_images = models.TextField(null=True, blank=True, default=None)
    ncb_images_logs = models.TextField(null=True, blank=True, default=None)
    ncb_latest_submitted_at = models.DateTimeField(null=True, blank=True, default=None) # To-Do: changed from ncb_latest_submitted   

    created_at = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated_at = models.DateTimeField(null=True, blank=True, default=None)

    def __str__(self):
        return str(self.user.first_name) + ' '  + str(self.user.last_name) + ' (' + str(self.user.email) + ')'

class UserManifestAdmin(admin.ModelAdmin):
    search_fields=['user__tvid', 'user__uid', 'user__first_name', 'user__last_name', 'user__email', 'user__mobile_number', 'user__national_id']

class UserCorporate(models.Model): # To-Do: changed from Corporate
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    tax_id = models.CharField(max_length=32, null=True, blank=True, default=None) # to-do: changed from corp_id
    name_th = models.CharField(max_length=128, null=True, blank=True, default=None) # To-Do: changed from corp_name_th
    name_en = models.CharField(max_length=128, null=True, blank=True, default=None) # To-Do: changed from corp_name
    category = models.CharField(max_length=128, null=True, blank=True, default=None) # To-Do: changed from corp_category
    category_other = models.CharField(max_length=128, null=True, blank=True, default=None) # To-Do: changed from corp_category_other
    address = models.CharField(max_length=128, null=True, blank=True, default=None)
    street = models.CharField(max_length=64, null=True, blank=True, default=None)
    subdistrict = models.CharField(max_length=64, null=True, blank=True, default=None)
    district = models.CharField(max_length=64, null=True, blank=True, default=None)
    province = models.CharField(max_length=64, null=True, blank=True, default=None)
    postal_code = models.CharField(max_length=8, null=True, blank=True, default=None)
    phone = models.CharField(max_length=32, null=True, blank=True, default=None)
    created_at = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated_at = models.DateTimeField(null=True, blank=True, default=None)

    def __str__(self):
        return str(self.name_th) + ' ' + '(' + str(self.user.email) + ')'

class UserCorporateAdmin(admin.ModelAdmin):
    search_fields=['tax_id', 'name_th', 'name_en', 'user__tvid', 'user__uid', 'user__first_name', 'user__last_name', 'user__email', 'user__mobile_number', 'user__national_id']

class Notification(models.Model):
    id = models.AutoField(primary_key=True)
    uid = models.CharField(max_length=32) # To-Do: implement
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, default=None)
    status = models.CharField(max_length=16, default='')
    family = models.CharField(max_length=16, null=True, blank=True, default=None)
    kind = models.CharField(max_length=16, default='')
    action_type = models.CharField(max_length=16, default='')
    action_screen = models.CharField(max_length=32, default='')
    title = models.CharField(max_length=160, default='')
    body = models.CharField(max_length=256, default='')
    created_at = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated_at = models.DateTimeField(null=True, blank=True, default=None)

    def __str__(self):
        return str(self.user.first_name) + ' ' + str(self.user.last_name) + ' ' + str(self.action_type) + ' ' + '(' + str(self.status) + ')'

class NotificationAdmin(admin.ModelAdmin):
    search_fields=['user__tvid', 'user__uid', 'user__first_name', 'user__last_name', 'user__email', 'user__mobile_number', 'user__national_id']

class Balance(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    account_no = models.CharField(max_length=64, default=None) # To-Do: changed from account_vid
    cash_balance = models.FloatField(default=0)
    as_of = models.CharField(max_length=32)
    created_at = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated_at = models.DateTimeField(null=True, blank=True, default=None)
    
    def __str__(self):
        return str(self.user.first_name) + ' ' + str(self.user.last_name) + ' ' + str(self.cash_balance)

class BalanceAdmin(admin.ModelAdmin):
    search_fields=['user__tvid', 'user__uid', 'user__first_name', 'user__last_name', 'user__email', 'user__mobile_number', 'user__national_id']

class MorningBalance(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    account_no = models.CharField(max_length=64, default=None) # To-Do: changed from account_vid
    cash_balance = models.FloatField(default=0)
    as_of = models.CharField(max_length=32)
    created_at = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated_at = models.DateTimeField(null=True, blank=True, default=None)
    
    def __str__(self):
        return str(self.user.first_name) + ' ' + str(self.user.last_name) + ' ' + str(self.cash_balance)

class MorningBalanceAdmin(admin.ModelAdmin):
    search_fields=['user__tvid', 'user__uid', 'user__first_name', 'user__last_name', 'user__email', 'user__mobile_number', 'user__national_id']

class Wallet(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    kind = models.CharField(max_length=16, default=None)
    value = models.FloatField(null=True, blank=True, default=0)
    amount = models.FloatField(default=0)
    balance = models.FloatField(default=0)
    reference = models.CharField(max_length=255, default=None)
    status = models.CharField(max_length=32, null=True, blank=True, default=None)
    created_at = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated_at = models.DateTimeField(null=True, blank=True, default=None)
    
    def __str__(self):
        return str(self.user.first_name) + ' ' + str(self.user.last_name) + ' ' + str(self.kind)

class WalletAdmin(admin.ModelAdmin):
    search_fields=['user__tvid', 'user__uid', 'user__first_name', 'user__last_name', 'user__email', 'user__mobile_number', 'user__national_id']

class InvestPreference(models.Model): # To-Do: changed from Investpreference
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    max_ltv = models.FloatField(default=0)
    max_tenors = models.IntegerField(default=0)
    max_invest = models.IntegerField(null=True, blank=True, default=10000)
    max_group = models.IntegerField(null=True, blank=True, default=0)
    outstanding_invested = models.IntegerField(null=True, blank=True, default=0)
    created_at = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated_at = models.DateTimeField(null=True, blank=True, default=None)

    def __str__(self):
        return str(self.user.first_name) + ' ' + str(self.user.last_name)

class InvestPreferenceAdmin(admin.ModelAdmin):
    search_fields=['user__tvid', 'user__uid', 'user__first_name', 'user__last_name', 'user__email', 'user__mobile_number', 'user__national_id']

class Portfolio(models.Model):
    id = models.AutoField(primary_key=True) 
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    account_no = models.CharField(max_length=32)
    symbol = models.CharField(max_length=16)
    avail_vol = models.IntegerField(default=0)
    actual_vol = models.IntegerField(default=0)
    mkt_price = models.FloatField(default=0)
    amount = models.FloatField(default=0)
    as_of = models.CharField(max_length=32)
    created_at = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated_at = models.DateTimeField(null=True, blank=True, default=None)

    def __str__(self):
        return str(self.user.first_name) + ' ' + str(self.user.last_name)

class PortfolioAdmin(admin.ModelAdmin):
    search_fields=['user__tvid', 'user__uid', 'user__first_name', 'user__last_name', 'user__email', 'user__mobile_number', 'user__national_id']

class PortfolioLog(models.Model): # To-Do: changed from Portfoliolog
    id = models.AutoField(primary_key=True) 
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    data = models.TextField(default=None)
    created_at = models.DateTimeField(auto_now_add=True, auto_now=False)

    def __str__(self):
        return str(self.user.first_name) + ' ' + str(self.user.last_name)

class PortfolioLogAdmin(admin.ModelAdmin):
    search_fields=['user__tvid', 'user__uid', 'user__first_name', 'user__last_name', 'user__email', 'user__mobile_number', 'user__national_id']

class Stock(models.Model):
    id = models.AutoField(primary_key=True)
    symbol = models.CharField(max_length=16, unique=True)
    excerpt = models.CharField(max_length=64)
    set_group = models.CharField(max_length=8, default='')
    ntf_group = models.CharField(max_length=8, default='')
    ntf_group_max = models.IntegerField(null=True, blank=True, default=0)
    par_price = models.FloatField(null=True, blank=True, default=0)
    par_price_at = models.CharField(max_length=32, null=True, blank=True, default=None)
    listed_share = models.BigIntegerField(null=True, blank=True, default=0)
    listed_share_at = models.CharField(max_length=32, null=True, blank=True, default=None)
    created_at = models.DateTimeField(auto_now_add=True, auto_now=False)
    
    def __str__(self):
        return str(self.symbol) + ' ' +  'MAX' + str(self.ntf_group_max)

class StockAdmin(admin.ModelAdmin):
    search_fields=['symbol']

class StockPrice(models.Model): # To-Do: changed from Stockprice
    id = models.AutoField(primary_key=True)
    symbol = models.CharField(max_length=16)
    prior_close_price = models.FloatField(default=0)
    board_lot = models.IntegerField(default=0)
    last_price = models.FloatField(default=0)
    proj_price = models.FloatField(default=0)
    ceiling_price = models.FloatField(default=0)
    floor_price = models.FloatField(default=0)
    as_of = models.CharField(max_length=32)
    created_at = models.DateTimeField(auto_now_add=True, auto_now=False)

    def __str__(self):
        return str(self.symbol) + ' ' +  '(' + str(self.prior_close_price) + ')'

class StockPriceAdmin(admin.ModelAdmin):
    search_fields=['symbol']

class Loan(models.Model):
    id = models.AutoField(primary_key=True)
    uid = models.CharField(unique=True, max_length=128)
    ref = models.CharField(unique=True, max_length=16, null=True, blank=True, default=None)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    user_level = models.CharField(max_length=8, null=True, blank=True, default=None)
    user_level_token = models.TextField(null=True, blank=True, default=None)
    user_level_confirmed = models.CharField(max_length=8, null=True, blank=True, default=None)
    user_level_confirmed_at = models.DateTimeField(null=True, blank=True, default=None)
    status = models.CharField(max_length=32, default='')
    
    purpose = models.CharField(max_length=16, default='')
    business_data = models.TextField(null=True, blank=True, default=None)

    tenors = models.FloatField(default=0)
    due_date = models.DateField(null=True, blank=True, default=None)

    portfolio = models.TextField(default='')
    asset_amount = models.IntegerField(default=0)
    shares_amount = models.IntegerField(default=0)
    actual_portfolio = models.TextField(null=True, blank=True, default=None)
    actual_portfolio_updated_at = models.DateTimeField(null=True, blank=True, default=None) # To-Do: implement

    total_amount = models.FloatField(default=0)
    total_amount_diff_ratio = models.FloatField(null=True, blank=True, default=0) # To-Do: changed from diff_ratio
    average_interest = models.FloatField(default=0) # To-Do: changed from interest
    avarage_fee = models.FloatField(default=0) # To-Do: changed from fee
    interest_data = models.TextField(null=True, blank=True, default=None)
    actual_total_amount = models.FloatField(null=True, blank=True, default=0)
    actual_average_interest = models.FloatField(null=True, blank=True, default=0) # To-Do: changed from actual_interest
    actual_avarage_fee = models.FloatField(null=True, blank=True, default=0) # To-Do: changed from actual_fee
    actual_interest_data = models.TextField(null=True, blank=True, default=None)
    actual_updated_at = models.DateTimeField(null=True, blank=True, default=None)
    actual_confirmed_at = models.DateTimeField(null=True, blank=True, default=None) # To-Do: changed from submit_confirmed_at
    
    approved_counter = models.IntegerField(null=True, blank=True, default=0)
    approved_by = models.CharField(max_length=256, null=True, blank=True, default=None)
    rejected_counter = models.IntegerField(null=True, blank=True, default=0)
    rejected_by = models.CharField(max_length=256, null=True, blank=True, default=None)
    approved_at = models.DateTimeField(null=True, blank=True, default=None)
    rejected_at = models.DateTimeField(null=True, blank=True, default=None) # To-Do: implement
    
    cancel_reject_message = models.TextField(null=True, blank=True, default=None) # To-Do: implement
    flag = models.TextField(null=True, blank=True, default=None) # To-Do: implement
    remark = models.TextField(null=True, blank=True, default=None)
    logs = models.TextField(null=True, blank=True, default=None)

    rpa_state = models.CharField(max_length=32, null=True, blank=True, default=None)

    created_at = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated_at = models.DateTimeField(null=True, blank=True, default=None)

    def __str__(self):
        return str(self.user.first_name) + ' ' + str(self.user.last_name) + ' ' + str(self.actual_total_amount) + ' ' + '(' + self.status + ')'

class LoanAdmin(admin.ModelAdmin):
    search_fields=['uid', 'ref', 'user__tvid', 'user__uid', 'user__first_name', 'user__last_name', 'user__email', 'user__mobile_number', 'user__national_id']

class Contract(models.Model):
    id = models.AutoField(primary_key=True)
    uid = models.CharField(unique=True, max_length=128)
    ref = models.CharField(unique=True, max_length=16, null=True, blank=True, default=None) # To-Do: implement
    loan = models.ForeignKey(Loan, on_delete=models.CASCADE)
    status = models.CharField(max_length=32, default='')
    
    ntf_group = models.CharField(max_length=16, default='')
    ntf_group_max = models.IntegerField(null=True, blank=True, default=0)
    selected_ltv = models.FloatField(null=True, blank=True, default=0)
    current_ltv = models.FloatField(null=True, blank=True, default=0)
    current_ltv_at = models.DateTimeField(null=True, blank=True, default=None)
    
    interest = models.FloatField(null=True, blank=True, default=0)
    effective_interest = models.FloatField(null=True, blank=True, default=0)
    fee = models.FloatField(null=True, blank=True, default=0)
    effective_fee = models.FloatField(null=True, blank=True, default=0)
    total_collateral = models.FloatField(null=True, blank=True, default=0) # To-Do: implement (from lona interest_data['sum_gx])
    total_amount = models.FloatField(null=True, blank=True, default=0)
    total_interest = models.FloatField(null=True, blank=True, default=0)
    total_fee = models.FloatField(null=True, blank=True, default=0)
    total_vat = models.FloatField(null=True, blank=True, default=0)
    total_stamp = models.FloatField(null=True, blank=True, default=0)
    transaction_amount = models.IntegerField(default=0) # To-Do: changed from total_transaction
    shares_amount = models.IntegerField(default=0) # To-Do: changed from total_share
    portfolio = models.TextField(null=True, blank=True, default='') # To-Do: implement

    signed_by = models.CharField(max_length=256, null=True, blank=True, default=None)
    signed_at = models.DateTimeField(null=True, blank=True, default=None)

    flag = models.TextField(null=True, blank=True, default=None) # To-Do: implement
    remark = models.TextField(null=True, blank=True, default=None)
    logs = models.TextField(null=True, blank=True, default=None)

    created_at = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated_at = models.DateTimeField(null=True, blank=True, default=None)
    canceled_at = models.DateTimeField(null=True, blank=True, default=None) # To-Do: implement
    active_at = models.DateTimeField(null=True, blank=True, default=None) # To-Do: implement
    completed_at = models.DateTimeField(null=True, blank=True, default=None) # To-Do: implement

    def __str__(self):
        return str(self.loan.user.first_name) + ' ' + str(self.loan.user.last_name) + ' ' + 'MAX' + str(self.ntf_group_max) + ' ' + str(self.total_amount) + ' ' + '(' + self.status + ')'

class ContractAdmin(admin.ModelAdmin):
    search_fields=['uid', 'loan__uid', 'loan__ref', 'loan__user__tvid', 'loan__user__uid', 'loan__user__first_name', 'loan__user__last_name', 'loan__user__email', 'loan__user__mobile_number', 'loan__user__national_id']

class ContractMatch(models.Model): # To-Do: changed from Contractmatch
    id = models.AutoField(primary_key=True)
    uid = models.CharField(unique=True, max_length=32) # To-Do: change algorithm to match max_length
    loan = models.ForeignKey(Loan, on_delete=models.CASCADE)
    contract = models.ForeignKey(Contract, on_delete=models.CASCADE)
    investor = models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.CharField(max_length=32, default='')
    invest_amount = models.FloatField(default=0)
    divider = models.FloatField(default=0)
    before_investment = models.FloatField(default=0)
    after_investment = models.FloatField(default=0)
    created_at = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated_at = models.DateTimeField(null=True, blank=True, default=None)

    def __str__(self):
        return str(self.investor.first_name) + ' ' + str(self.investor.last_name) + ' ' + 'invested to ' + str(self.loan.user.first_name) + ' ' + str(self.loan.user.last_name) + ' ' +  str(self.invest_amount) + ' ' + '(' + self.status + ')'

class ContractMatchAdmin(admin.ModelAdmin):
    search_fields=['contract__uid', 'contract__ref']

class ShareTransaction(models.Model): # To-Do: changed from Sharetransaction
    id = models.AutoField(primary_key=True)
    uid = models.CharField(unique=True, max_length=32)
    contract = models.ForeignKey(Contract, on_delete=models.CASCADE)
    status = models.CharField(max_length=16, default='')
    account_no = models.CharField(max_length=32)
    symbol = models.CharField(max_length=16)
    amount = models.IntegerField(default=0)
    price = models.FloatField(default=0)
    lock_staging = models.CharField(max_length=8, default='')
    pledge_staging = models.CharField(max_length=8, default='')
    created_at = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated_at = models.DateTimeField(null=True, blank=True, default=None)

    def __str__(self):
        return str(self.contract.ref) + ' ' + '(' + self.status + ')'

class ShareTransactionAdmin(admin.ModelAdmin):
    search_fields=['contract__uid', 'contract__ref']

class TransactionLog(models.Model): # To-Do: changed from Transactionlog
    id = models.AutoField(primary_key=True)
    bid = models.CharField(max_length=255, null=True, blank=True, default='')
    status = models.CharField(max_length=16, default='')
    request_id = models.CharField(max_length=64, null=True, blank=True, default='')
    request_func = models.CharField(max_length=64, default='')
    request_by = models.CharField(max_length=8, default='')
    request_to = models.CharField(max_length=8, default='')
    request_body = models.TextField(default='')
    response_data = models.TextField(default='')
    reference = models.CharField(max_length=255, null=True, blank=True, default=None)
    flag = models.TextField(null=True, blank=True, default=None) # To-Do: implement
    created_at = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated_at = models.DateTimeField(null=True, blank=True, default=None)

    def __str__(self):
        return str(self.request_func) + ' ' + '(' + self.status + ')' + ' ' + str(self.created_at)

class TransferStage(models.Model): # To-Do: changed from Transferstage
    id = models.AutoField(primary_key=True)
    uid = models.CharField(unique=True, max_length=32)
    bid = models.CharField(max_length=255, null=True, blank=True, default='')
    contract = models.ForeignKey(Contract, on_delete=models.CASCADE, null=True, blank=True, default=None)
    status = models.CharField(max_length=16, default='')
    kind = models.CharField(max_length=32) 
    data = models.TextField()
    flag = models.TextField(null=True, blank=True, default=None) # To-Do: implement
    created_at = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated_at = models.DateTimeField(null=True, blank=True, default=None)

    def __str__(self):
        return str(self.kind) + ' ' + str(self.contract.ref) + ' ' + '(' + self.status + ')' + ' ' + str(self.created_at)

class TransferLog(models.Model): # To-Do: changed from Transferlog
    id = models.AutoField(primary_key=True)
    uid = models.CharField(unique=True, max_length=32)
    bid = models.CharField(max_length=255, null=True, blank=True, default='')
    contract = models.ForeignKey(Contract, on_delete=models.CASCADE, null=True, blank=True, default=None)
    status = models.CharField(max_length=16, default='')
    trans_type = models.CharField(max_length=16, default='')
    trans_purpose = models.CharField(max_length=64, default='')
    tvid = models.CharField(max_length=255, default='')
    amount = models.FloatField(default=0)
    flag = models.CharField(max_length=16, null=True, blank=True, default='')
    created_at = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated_at = models.DateTimeField(null=True, blank=True, default=None)

    def __str__(self):
        return str(self.trans_type) + ' ' + str(self.trans_purpose) + ' ' + str(self.contract.ref) + ' ' + '(' + self.status + ')' + ' ' + str(self.created_at)

class TransferLogAdmin(admin.ModelAdmin):
    search_fields=['contract__uid', 'tvid', 'flag']

class MatchingLog(models.Model):
    id = models.AutoField(primary_key=True)
    uid = models.CharField(max_length=32) # To-Do: implement
    status = models.CharField(max_length=16, default='')
    title = models.CharField(max_length=160, default='')
    version = models.CharField(max_length=32, null=True, blank=True, default=None) # To-Do: changed from family
    body = models.TextField(default='')
    pool = models.TextField(default='')
    created_at = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated_at = models.DateTimeField(null=True, blank=True, default=None) # To-Do: implement

    def __str__(self):
        return str(self.title) + ' ' + str(self.version)

class Metadata(models.Model): # To-Do: changed from Meta
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=16, unique=True)
    value = models.TextField(null=True, blank=True, default=None)
    created_at = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated_at = models.DateTimeField(null=True, blank=True, default=None)

    def __str__(self):
        return str(self.name) + ' ' + str(self.updated_at)

class Report(models.Model):
    id = models.AutoField(primary_key=True)
    month = models.CharField(max_length=8)
    dataset = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated_at = models.DateTimeField(null=True, blank=True, default=None) # To-Do: implement

    def __str__(self):
        return str(self.month) + ' ' + str(self.created_at)

class RPAJob(models.Model):
    id = models.AutoField(primary_key=True)
    uid = models.CharField(unique=True, max_length=32)
    kind = models.CharField(max_length=16, null=True, blank=True, default=None)
    name = models.CharField(max_length=32, default='')
    start_time = models.DateTimeField(default=None)
    start_with = models.CharField(max_length=32, default='')
    total_generated_task = models.IntegerField(null=True, blank=True, default=0)
    total_run_task = models.IntegerField(null=True, blank=True, default=0)
    total_skipped_task = models.IntegerField(null=True, blank=True, default=0)
    completed_at = models.DateTimeField(null=True, blank=True, default=None)
    status = models.CharField(max_length=16, default='')
    created_at = models.DateTimeField(auto_now_add=True, auto_now=False)

    def __str__(self):
        return str(self.name) + ' ' + str(self.kind)

class RPATask(models.Model):
    id = models.AutoField(primary_key=True)
    uid = models.CharField(unique=True, max_length=32)
    job = models.ForeignKey(RPAJob, on_delete=models.CASCADE)
    status = models.CharField(max_length=16, default='')
    ordering_weight = models.IntegerField(default=0)
    process_name = models.CharField(max_length=32, default='')
    request_id = models.CharField(max_length=64, default='')
    reference_class = models.CharField(max_length=16, default='')
    reference_id = models.CharField(max_length=128, default='') 
    flag = models.CharField(max_length=128, null=True, blank=True, default='') 
    created_at = models.DateTimeField(auto_now_add=True, auto_now=False)
    executed_at = models.DateTimeField(null=True, blank=True, default=None)

    def __str__(self):
        return str(self.job.name) + ' ' + str(self.ordering_weight) + ' ' + str(self.process_name) + ' ' + str(self.flag)
