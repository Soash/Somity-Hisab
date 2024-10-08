from django.urls import path
from . import views

urlpatterns = [
    path('', views.signin, name='login'),
    path('logout/', views.signout, name='logout'),
    path('home/', views.home, name='home'),
    path('customer_home/', views.customer_home, name='customer_home'),
    path('update-active-branch/', views.update_active_branch, name='update_active_branch'),
    path('set_language/', views.set_language, name='set_language'),
    path('customer-login/', views.customer_login, name='customer_login'),
    path('customer-logout/', views.customer_signout, name='customer_logout'),
    path('customer_change_password/', views.customer_change_password, name='customer_change_password'),
    path('access-denied/', views.access_denied, name='access_denied'),

    path('manage-permissions/', views.manage_permissions, name='manage_permissions'),

    path('customers-add/', views.customer_add, name='customer_add'),
    path('customers-list/', views.customer_list, name='customer_list'),
    path('customers-details/<int:id>/', views.customer_details, name='customer_details'),
    path('customers-edit/<int:id>/', views.customer_edit, name='customer_edit'),

    path('general-list/', views.general_list, name='general_list'),
    path('general-deposit/<int:id>/', views.general_deposit, name='general_deposit'),
    path('general-withdraw/<int:id>/', views.general_withdraw, name='general_withdraw'),
    path('general-transactions/<int:id>/', views.general_transaction_history, name='general_transaction_history'),
    path('general-deposit-search/', views.general_deposit_search, name='general_deposit_search'),
    path('general-withdraw-search/', views.general_withdraw_search, name='general_withdraw_search'),

    path('savings-list/', views.savings_list, name='savings_list'),
    path('savings-deposit/<int:id>/', views.savings_deposit, name='savings_deposit'),
    path('savings-withdraw/<int:id>/', views.savings_withdraw, name='savings_withdraw'),
    path('savings-transactions/<int:id>/', views.savings_transaction_history, name='savings_transaction_history'),
    path('savings-deposit-search/', views.savings_deposit_search, name='savings_deposit_search'),
    path('savings-withdraw-search/', views.savings_withdraw_search, name='savings_withdraw_search'),

    path('loan-search/', views.loan_search, name='loan_search'),
    path('loan-list/', views.loan_list, name='loan_list'),
    path('loan-create/<str:account_no>/', views.loan_create, name='loan_create'),
    path('loan-schedule/<int:loan_id>/', views.loan_schedule, name='loan_schedule'),
    path('loan-collection/<int:loan_id>/', views.loan_collection, name='loan_collection'),
    path('loan-transaction/<int:loan_id>/', views.loan_trans, name='loan_trans'),
    path('loan-fine/<int:loan_id>/', views.loan_fine, name='loan_fine'),
    path('loan-collection-search/', views.loan_collection_search, name='loan_collection_search'),
    path('loan-close-search/', views.loan_close_search, name='loan_close_search'),
    path('loan-close/<int:loan_id>/', views.loan_close, name='loan_close'),



    path('loan-cc-search/', views.loan_cc_search, name='loan_cc_search'),
    path('loan-cc-list/', views.loan_cc_list, name='loan_cc_list'),
    path('loan-cc-create/<str:account_no>/', views.loan_cc_create, name='loan_cc_create'),
    path('loan-cc-collection/<int:loan_id>/', views.loan_cc_collection, name='loan_cc_collection'),
    path('loan-cc-transaction/<int:loan_id>/', views.loan_cc_trans, name='loan_cc_trans'),
    path('loan-cc-collection-search/', views.loan_cc_collection_search, name='loan_cc_collection_search'),
    path('loan-cc-close-search/', views.loan_cc_close_search, name='loan_cc_close_search'),
    path('loan-cc-close/<int:loan_id>/', views.loan_cc_close, name='loan_cc_close'),


    path('loan-special-search/', views.loan_sp_search, name='loan_sp_search'),
    path('loan-special-list/', views.loan_sp_list, name='loan_sp_list'),
    path('loan-special-create/<str:account_no>/', views.loan_sp_create, name='loan_sp_create'),
    path('loan-special-collection/<int:loan_id>/', views.loan_sp_collection, name='loan_sp_collection'),
    path('loan-special-close-search/', views.loan_sp_close_search, name='loan_sp_close_search'),
    path('loan-special-close/<int:loan_id>/', views.loan_sp_close, name='loan_sp_close'),



    path('dps-search/', views.dps_search, name='dps_search'),
    path('dps-list/', views.dps_list, name='dps_list'),
    path('dps-create/<str:account_no>/', views.dps_create, name='dps_create'),
    path('dps-schedule/<int:id>/', views.dps_schedule, name='dps_schedule'),
    path('dps-deposit/<int:id>/', views.dps_deposit, name='dps_deposit'),
    path('dps-withdraw/<int:id>/', views.dps_withdraw, name='dps_withdraw'),
    path('dps-transaction/<int:id>/', views.dps_transaction, name='dps_transaction'),
    path('dps-deposit-search/', views.dps_deposit_search, name='dps_deposit_search'),
    path('dps-withdraw-search/', views.dps_withdraw_search, name='dps_withdraw_search'),
    path('dps-close-search/', views.dps_close_search, name='dps_close_search'),
    path('dps-close/<int:id>/', views.dps_close, name='dps_close'),

    path('fdr-search/', views.fdr_search, name='fdr_search'),
    path('fdr-list/', views.fdr_list, name='fdr_list'),
    path('fdr-create/<str:account_no>/', views.fdr_create, name='fdr_create'),
    path('fdr-deposit/<int:id>/', views.fdr_deposit, name='fdr_deposit'),
    path('fdr-withdraw/<int:id>/', views.fdr_withdraw, name='fdr_withdraw'),
    path('fdr-profit-withdraw/<int:id>/', views.fdr_profit_withdraw, name='fdr_profit_withdraw'),
    path('fdr-transactions/<int:id>/', views.fdr_transaction_history, name='fdr_transaction_history'),
    path('fdr-profit/<int:id>/', views.fdr_profit, name='fdr_profit'),
    path('fdr-deposit-search/', views.fdr_deposit_search, name='fdr_deposit_search'),
    path('fdr-profit-withdraw-search/', views.fdr_profit_withdraw_search, name='fdr_profit_withdraw_search'),
    path('fdr-balance-withdraw-search/', views.fdr_balance_withdraw_search, name='fdr_balance_withdraw_search'),
    path('fdr-close-search/', views.fdr_close_search, name='fdr_close_search'),
    path('fdr-close/<int:id>/', views.fdr_close, name='fdr_close'),

    path('share-list/', views.share_list, name='share_list'),
    path('share-create/<str:account_no>/', views.share_create, name='share_create'),
    path('share-search/', views.share_search, name='share_search'),
    path('share-deposit/<int:share_id>/', views.share_deposit, name='share_deposit'),
    path('share-deposit-search/', views.share_deposit_search, name='share_deposit_search'),
    path('share-withdraw-search/', views.share_withdraw_search, name='share_withdraw_search'),
    path('share-profit-withdraw-search/', views.share_profit_withdraw_search, name='share_profit_withdraw_search'),
    path('share-withdraw/<int:share_id>/', views.share_withdraw, name='share_withdraw'),
    path('share-transfer/<int:share_id>/', views.share_transfer, name='share_transfer'),
    path('share-profit-withdraw/<int:share_id>/', views.share_profit_withdraw, name='share_profit_withdraw'),
    path('share-transaction-history/<int:share_id>/', views.share_transaction_history, name='share_transaction_history'),

    path('bank_withdraw/', views.bank_withdraw, name='bank_withdraw'),
    path('bank_deposit/', views.bank_deposit, name='bank_deposit'),
    path('package/', views.package, name='package'),

    path('delete-search/', views.delete_search, name='delete_search'),
    path('delete-customer/<int:id>/', views.delete_customer, name='delete_customer'),
    path('delete-loan/<int:id>/', views.loan_delete, name='loan_delete'),
    path('delete-loan-cc/<int:id>/', views.loan_cc_delete, name='loan_cc_delete'),
    path('delete-loan-sp/<int:id>/', views.loan_sp_delete, name='loan_sp_delete'),
    path('delete-dps/<int:id>/', views.dps_delete, name='dps_delete'),
    path('delete-fdr/<int:id>/', views.fdr_delete, name='fdr_delete'),
    path('delete-share/<int:share_id>/', views.share_delete, name='share_delete'),

    path('somity_wise_dps_deposit/', views.somity_wise_dps_deposit, name='somity_wise_dps_deposit'),
    path('somity_wise_general_deposit/', views.somity_wise_general_deposit, name='somity_wise_general_deposit'),
    path('somity_wise_loan/', views.somity_wise_loan, name='somity_wise_loan'),
    path('common_collection/', views.common_collection, name='common_collection'),
]