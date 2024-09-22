/** @leewise-module */

import { Component } from "@leewise/owl";

export class AccountReportEllipsisPopover extends Component {
    static template = "account_reports.AccountReportEllipsisPopover";
    static props = {
        close: Function,
        name: String,
        copyEllipsisText: Function,
    };
}
