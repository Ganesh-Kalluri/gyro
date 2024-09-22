/* @leewise-module */

import { Component } from "@leewise/owl";

export class MessageNotificationPopover extends Component {
    static template = "mail.MessageNotificationPopover";
    static props = ["message", "close?"];
}
