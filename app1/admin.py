from django.contrib import admin
from .models import Customer, ActiveBranch, DPSDeposit, LoanAC, InstallmentSchedule, LoanCollection, DPS, DPSInstallmentSchedule
from .models import GeneralAC, GeneralWithdraw, GeneralDeposit, FDR, FDRTransactionHistory, SavingsAC, ShareAC
from django.contrib import admin
from .models import ProfitHistory

class ActiveBranchAdmin(admin.ModelAdmin):
    list_display = ('branch', 'user')

class CustomerAdmin(admin.ModelAdmin):
    list_display = ('id','customer_name', 'branch', 'processed_by')

from django.contrib import admin
from .models import Customer
from .forms import CustomerAdminForm

# class CustomerAdmin(admin.ModelAdmin):
#     form = CustomerAdminForm
#     list_display = ('account_no', 'customer_name', 'mobile_number', 'branch', 'status')
#     search_fields = ('account_no', 'customer_name', 'mobile_number')



class GeneralACAdmin(admin.ModelAdmin):
    list_display = ('id','customer', 'status')

class SavingsACAdmin(admin.ModelAdmin):
    list_display = ('id','customer', 'status')

class ShareACAdmin(admin.ModelAdmin):
    list_display = ('customer', 'balance')

class GeneralDepositAdmin(admin.ModelAdmin):
    list_display = ('VoucherID', 'Amount', 'Note', 'created_at', 'processed_by', 'general')
    search_fields = ('VoucherID', 'Note', 'processed_by')
    list_filter = ('created_at', 'processed_by')
    ordering = ('-created_at',)



class GeneralWithdrawAdmin(admin.ModelAdmin):
    list_display = ('VoucherID', 'Amount', 'Note', 'created_at', 'processed_by', 'general')
    search_fields = ('VoucherID', 'Note', 'processed_by')
    list_filter = ('created_at', 'processed_by')
    ordering = ('-created_at',)

class FDRAdmin(admin.ModelAdmin):
    list_display = ('opening_amount', 'duration', 'monthly_profit_percentage', 'last_profit_added')

class FDRTransactionHistoryAdmin(admin.ModelAdmin):
    list_display = ('fdr', 'transaction_type', 'created_at')


class ProfitHistoryAdmin(admin.ModelAdmin):
    list_display = ('fdr', 'profit_added', 'available_profit', 'added_on')
    list_filter = ('added_on', 'fdr')
    search_fields = ('fdr__transaction_id', 'profit_added', 'available_profit')




class LoanACAdmin(admin.ModelAdmin):
    list_display = ('id', 'customer')

class LoanCollectionAdmin(admin.ModelAdmin):
    list_display = ('loan', 'Amount')



class DPSAdmin(admin.ModelAdmin):

    list_display = ('customer', 'branch', 'created_date', 'total_amount', 'processed_by')
    search_fields = ('customer__name', 'transaction_id')
    list_filter = ('branch', 'created_date')




class DPSInstallmentScheduleAdmin(admin.ModelAdmin):
    list_display = ('dps', 'installment_number', 'amount', 'due_date', 'skipped_due_date', 'installment_status')
    list_editable = ('installment_status',)  



class InstallmentScheduleAdmin(admin.ModelAdmin):
    list_display = ('loan', 'installment_number', 'amount', 'due_date', 'skipped_due_date', 'installment_status')
    list_editable = ('installment_status',)  




admin.site.register(Customer, CustomerAdmin)
# admin.site.register(GeneralAC, GeneralACAdmin)
# admin.site.register(SavingsAC, SavingsACAdmin)
# admin.site.register(ShareAC, ShareACAdmin)
# admin.site.register(DPS, DPSAdmin)
admin.site.register(ActiveBranch, ActiveBranchAdmin)
# admin.site.register(LoanAC)
# admin.site.register(DPSDeposit)
# admin.site.register(InstallmentSchedule, InstallmentScheduleAdmin)
# admin.site.register(LoanCollection, LoanCollectionAdmin)
# admin.site.register(DPSInstallmentSchedule, DPSInstallmentScheduleAdmin)
# admin.site.register(FDR, FDRAdmin)
# admin.site.register(GeneralDeposit, GeneralDepositAdmin)
# admin.site.register(GeneralWithdraw, GeneralWithdrawAdmin)
# admin.site.register(FDRTransactionHistory, FDRTransactionHistoryAdmin)
# admin.site.register(ProfitHistory, ProfitHistoryAdmin)

