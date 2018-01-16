odoo.define('arabic_receipt_posbox_less.posreceipt', function(require){
"use strict";
    var screens = require('point_of_sale.screens');
    var Model = require('web.Model');
    var models = require('point_of_sale.models');
    var core = require('web.core');
    var _t = core._t;
    var QWeb = core.qweb;


    screens.ReceiptScreenWidget.include({

    print_xml: function() {
        var self = this;
        var ord = this.pos.get_order();
        if(self.pos.config.arabic_allow)
        {

        var dataa = {
            receipt: ord.export_for_printing(),
            pr_ip: self.pos.config.proxy_ip,
            sh_dr: self.pos.config.iface_cashdrawer,
            ar_al: self.pos.config.arabic_allow
        };
        new Model('pos.order').call('pos_malik', [dataa]);

        }
        else{
            this._super();
        }
    },


    });

});