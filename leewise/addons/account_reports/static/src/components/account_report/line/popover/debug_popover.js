/** @leewise-module */

import { Component } from "@leewise/owl";

export class AccountReportDebugPopover extends Component {
    static template = "account_reports.AccountReportDebugPopover";
    static props = {
        close: Function,
        expressionsDetail: Array,
        onClose: Function,
    };
}
