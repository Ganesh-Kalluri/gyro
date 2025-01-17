/** @leewise-module */
import { Component } from "@leewise/owl";

export class ViewEditorSnackbar extends Component {
    static template = "web_studio.ViewEditor.Snackbar";
    static props = {
        operations: Object,
        saveIndicator: Object,
    };
}
