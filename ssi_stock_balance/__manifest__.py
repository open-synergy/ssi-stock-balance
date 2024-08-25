# Copyright 2024 OpenSynergy Indonesia
# Copyright 2024 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

{
    "name": "Stock Balance",
    "version": "14.0.1.6.0",
    "website": "https://simetri-sinergi.id",
    "author": "PT. Simetri Sinergi Indonesia, OpenSynergy Indonesia",
    "license": "AGPL-3",
    "installable": True,
    "depends": [
        "ssi_stock_account",
        "ssi_product",
        "ssi_master_data_mixin",
        "ssi_transaction_confirm_mixin",
        "ssi_transaction_done_mixin",
        "ssi_transaction_cancel_mixin",
        "ssi_transaction_date_duration_mixin",
        "ssi_m2o_configurator_mixin",
        "ssi_transaction_queue_done_mixin",
        "ssi_transaction_queue_cancel_mixin",
        "base_automation",
    ],
    "data": [
        "security/ir_module_category_data.xml",
        "security/res_group_data.xml",
        "security/ir.model.access.csv",
        "security/ir_rule_data.xml",
        "data/ir_sequence_data.xml",
        "data/sequence_template_data.xml",
        "data/policy_template_data.xml",
        "data/approval_template_data.xml",
        "data/ir_actions_server_data.xml",
        "data/base_automation_data.xml",
        "menu.xml",
        "views/stock_balance_type_views.xml",
        "views/stock_balance_views.xml",
        "views/product_product_views.xml",
        "views/product_stock_balance_views.xml",
        "views/product_stock_balance_warehouse_views.xml",
        "views/product_stock_balance_picking_views.xml",
    ],
    "demo": [],
    "images": [],
}