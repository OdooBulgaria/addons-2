# -*- coding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (C) 2004-2010 Tiny SPRL (<http://tiny.be>).
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################
# Generated by the OpenERP plugin for Dia !
from openerp.osv import fields,osv
class netpro_claim(osv.osv):
    _name = 'netpro.claim'
    _columns = {
        'claim_no': fields.char('Claim No.'),
        'claim_no_revision': fields.integer('Claim No Revision'),
        'ext_claim_no': fields.char('Ext Claim No'),
        'claim_date': fields.date('Claim Date'),
        'claim_received_date': fields.date('Claim Received Date'),
        'claim_loss_date_start': fields.date('Claim Loss Date Start'),
        'claim_loss_date_end': fields.date('Claim Loss Date End'),
        'policy_id': fields.many2one('netpro.policy', 'Policy'),
        'member_id': fields.many2one('netpro.member', 'Member'),
        'claim_category_id': fields.many2one('netpro.claim_category', 'Category'),
        'claim_type_id': fields.many2one('netpro.claim_type', 'Claim Type'),
        'diagnosis_id': fields.many2one('netpro.diagnosis', 'Diagnosis'),
        '2nd_diagnosis': fields.many2one('netpro.diagnosis', '2nd Diagnosis'),
        '3rd_diagnosis': fields.many2one('netpro.diagnosis', '3rd Diagnosis'),
        'claim_id': fields.many2one('netpro.claim', 'Main Claim No'),
        'branch_id': fields.many2one('netpro.branch', 'Branch'),
        'currency_id': fields.many2one('res.currency', 'Currency'),
        'claim_rate': fields.float('Claim Rate'),
        'policy_rate': fields.float('Policy Rate'),
        'reimbursement': fields.float('Reimbursement'),
        'claim_room_id': fields.many2one('netpro.claim_room', 'Room'),
        'exgratia_claim': fields.boolean('Exgratia Claim'),
        'non_jabodetabek': fields.boolean('Non-Jabodetabek'),
        'disable_prorate': fields.boolean('Disable Prorate'),
        'country_id': fields.many2one('res.country', 'Country'),
        'remarks': fields.text('Remarks'),
        'reason_id': fields.many2one('netpro.reason', 'Reason'),
        'other_reason': fields.text('Other Reason'),
        'sys_remarks': fields.text('Sys Remarks'),
        'discount': fields.float('Discount'),
        'aso_charge': fields.float('ASO Charge'),
        'reference_no': fields.char('Reference No'),
        'ref_tpa_payment': fields.char('Ref. TPA Payment'),
        'ref_excess': fields.char('Ref. Excess'),
        'pay_to': fields.many2one('res.partner', 'Pay To'),
        'payment_id': fields.many2one('res.partner', 'ID'),
        'account_no': fields.char('Account No'),
        'account_name': fields.char('Account Name'),
        'bank_id': fields.many2one('res.partner.bank', 'Bank'),
        'bank_name': fields.char('Bank Name'),
        'bank_branch': fields.char('Bank Branch'),
        'excess_payor_id': fields.many2one('netpro.excess_payor', 'Excess Payor'),
        'excess_id': fields.many2one('res.partner', 'Excess ID'),
        'excess_tpa_id': fields.many2one('netpro.tpa', 'Excess TPA ID'),
        'refund_account_no': fields.char('Account No'),
        'refund_account_name': fields.char('Account Name'),
        'refund_bank_name': fields.char('Bank Name'),
        'edc_trc_authorization': fields.char('TRC Authorization'),
        'edc_trc_claim_payable': fields.char('TRC Claim Payable'),
        'claim_status_id': fields.many2one('netpro.claim_status', 'Status'),
        'acceptation_status': fields.char('Acceptation Status'),
        'cno': fields.integer('CNO'),
        'pcno': fields.integer('PCNO'),
        'batch_id': fields.integer('Batch ID'),
        'glid': fields.integer('GL ID'),
        'prorate': fields.float('Prorate'),
        'payment_status_request_date': fields.date('Request Date'),
        'payment_status_payment_date': fields.date('Payment Date'),
        'payment_status_excess_payment_date': fields.date('Excess Payment Date'),
        'transaction_history_created_by_id': fields.many2one('res.partner', 'Created By'),
        'transaction_history_created_date': fields.datetime('Created Date'),
        'transaction_history_last_edited_by_id': fields.many2one('res.partner', 'Last Edited By'),
        'transaction_history_last_edited_date': fields.datetime('Last Edited By Date'),
        'transaction_history_adjusted_by_id': fields.many2one('res.partner', 'Adjusted By'),
        'transaction_history_adjusted_date': fields.date('Adjusted Date'),
        'transaction_history_checked_by_id': fields.many2one('res.partner', 'Checked By'),
        'transaction_history_checked_date': fields.date('Checked Date'),
        'transaction_history_released_by_id': fields.many2one('res.partner', 'Releases By'),
        'transaction_history_released_date': fields.date('Released Date'),
        'doctor': fields.char('Doctor'),
        'symptoms': fields.char('Symptoms'),
        'disease_history': fields.char('Disease History'),
        'phys_examination': fields.char('Phys. Examination'),
        'consultation': fields.char('Consultation'),
        'treatment_id': fields.many2one('netpro.treatment', 'Treatment'),
        'treatment_remarks': fields.text('Treatment Remarks'),
        'treatment_place': fields.char('Treatment Place'),
        'place_id': fields.many2one('netpro.place', 'Place'),
        'summary_billed': fields.float('Billed'),
        'sumary_unpaid': fields.float('Unpaid'),
        'summary_discount': fields.float('Discount'),
        'summary_cash_member': fields.float('Cash Member'),
        'summary_total_paid': fields.float('Total Paid'),
        'summary_accepted': fields.float('Accepted'),
        'summary_client_accepted': fields.float('Client Accepted'),
        'sumary_total_excess': fields.float('Total Excess'),
        'summary_cash_member_accepted': fields.float('Cash Member'),
        'summary_excess': fields.float('Excess (+)'),
        'summary_verified': fields.float('Verified'),
        'summary_adjustment': fields.float('Adjustment'),
        'summary_overall_limit': fields.float('Overall Limit'),
        'summary_usage': fields.float('Usage'),
        'summary_balance': fields.float('Balance'),
        'summary_family_limit': fields.float('Family Limit'),
        'summary_family_usage': fields.float('Family Usage'),
        'summary_family_balance': fields.float('Family Balance'),
        'summary_claim_count': fields.float('Claim Count'),
        'claim_detail_ids': fields.one2many('netpro.claim_detail', 'claim_id', 'Claim Details', ondelete='cascade'),
        'diagnosis_ids': fields.one2many('netpro.claim_diagnosis', 'claim_id', 'Diagnosis', ondelete='cascade'),
        'reason_ids': fields.one2many('netpro.reason', 'claim_id', 'Reasons', ondelete='cascade'),
    }
netpro_claim()

class netpro_claim_detail(osv.osv):
    _name = 'netpro.claim_detail'
    _columns = {
        'cno': fields.char('CNO'),
        'claim_id': fields.many2one('netpro.claim', 'Claim No'),
        'benefit_id': fields.many2one('netpro.benefit', 'Benefit'),
        'treatment_date_start': fields.date('Treatment Date Start'),
        'treatment_date_end': fields.date('Treatment Date End'),
        'quantity': fields.integer('Quantity'),
        'billed': fields.float('Billed'),
        'remarks': fields.text('Remarks'),
        'claim_detail_status_id': fields.many2one('netpro.claim_detail_status', 'Status'),
        'exclude': fields.boolean('Exclude'),
        'benefit_limit': fields.float('Benefit Limit'),
        'not_affectto_overall_limit': fields.boolean('Not Affect to Overall Limit'),
        'overall_limit': fields.float('Overall Limit'),
        'usage': fields.float('Usage'),
        'balance': fields.float('Balance'),
        'family_limit': fields.float('Family Limit'),
        'family_usage': fields.float('Family Usage'),
        'family_balance': fields.float('Family Balance'),
        'system_remarks': fields.text('System Remarks'),
        'verified': fields.float('Verified'),
        'excess': fields.float('Excess'),
        'accepted': fields.float('Accepted'),
        'unpaid': fields.float('Unpaid'),
        'cash_member': fields.float('Cash Member'),
        'client_accepted': fields.float('Client Accepted'),
        'quantity_verified': fields.integer('Quantity Verified'),
        'quantity_accepted': fields.integer('Quantity Accepted'),
        'reason_id': fields.many2one('netpro.reason', 'Reason'),
        'other_reason': fields.text('Other Reason'),
        'manual_verfied': fields.float('Manual Verfied'),
        'manual_excess': fields.float('Manual Excess'),
        'manual_accepted': fields.float('Manual Accepted'),
        'tolerance': fields.float('Tolerance'),
        'tolerance_days': fields.integer('Tolerance Days'),
        'claim_id': fields.many2one('netpro.claim', 'Claim'),
    }
netpro_claim_detail()

class netpro_diagnosis(osv.osv):
    _name = 'netpro.diagnosis'
    _columns = {
        'diagnosis': fields.char('Diagnosis'),
        'name': fields.char('Name'),
        'exclusion_F': fields.boolean('ExclusionF'),
        'pre_existing_f': fields.boolean('PreExistingF'),
        'standard_fee': fields.float('StandardFee'),
    }
netpro_diagnosis()

class netpro_claim_category(osv.osv):
    _name = 'netpro.claim_category'
    _columns = {
        'name': fields.char('Name'),
        'description': fields.text('Description'),
    }
netpro_claim_category()

class netpro_claim_type(osv.osv):
    _name = 'netpro.claim_type'
    _columns = {
        'name': fields.char('Name'),
        'description': fields.text('Description'),
    }
netpro_claim_type()

class netpro_claim_room(osv.osv):
    _name = 'netpro.claim_room'
    _columns = {
        'name': fields.char('Name'),
        'description': fields.text('Description'),
    }
netpro_claim_room()

class netpro_reason(osv.osv):
    _name = 'netpro.reason'
    _columns = {
        'name': fields.char('Name'),
        'description': fields.text('Description'),
        'claim_id': fields.many2one('netpro.claim', 'Claim'),
    }
netpro_reason()

class netpro_excess_payor(osv.osv):
    _name = 'netpro.excess_payor'
    _columns = {
        'name': fields.char('Name'),
        'description': fields.text('Description'),
    }
netpro_excess_payor()

class netpro_treatment(osv.osv):
    _name = 'netpro.treatment'
    _columns = {
        'treatment': fields.char('Treatment'),
        'name': fields.char('Name'),
        'treatment_category_id': fields.many2one('netpro.treatment_category', 'Treatment Category'),
        'description': fields.text('Description'),
    }
netpro_treatment()

class netpro_treatment_category(osv.osv):
    _name = 'netpro.treatment_category'
    _columns = {
        'name': fields.char('Name'),
        'description': fields.text('Description'),
    }
netpro_treatment_category()

class netpro_benefit(osv.osv):
    _name = 'netpro.benefit'
    _columns = {
        'benefit_id': fields.char('ID'),
        'name': fields.char('Name'),
        'reim': fields.float('Reim'),
        'provider_limit': fields.float('Provider Limit'),
        'non_provider_limit': fields.float('Non Provider Limit'),
        'unit': fields.char('Unit'),
        'usage': fields.float('Usage'),
        'remaining': fields.float('Remaining'),
    }
netpro_benefit()

class netpro_claim_detail_status(osv.osv):
    _name = 'netpro.claim_detail_status'
    _columns = {
        'name': fields.char('Name'),
        'description': fields.text('Description'),
    }
netpro_claim_detail_status()

class netpro_claim_diagnosis(osv.osv):
    _name = 'netpro.claim_diagnosis'
    _columns = {
        'claim_id': fields.many2one('netpro.claim', 'Claim'),
        'diagnosis': fields.char('Diagnosis ID'),
        'diagnosis_name': fields.char('Diagnosis Name'),
        'remarks': fields.char('Remarks'),
        'standard_fee': fields.float('Standard Fee'),
    }
netpro_claim_diagnosis()
