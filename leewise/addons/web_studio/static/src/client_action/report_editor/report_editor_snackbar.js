/** @leewise-module */
import { Component } from "@leewise/owl";

export class ReportEditorSnackbar extends Component {
    static template = "web_studio.ReportEditor.SnackBar";
    static props = {
        onSave: Function,
        state: Object,
        onDiscard: { type: Function, optional: true },
    };
}
