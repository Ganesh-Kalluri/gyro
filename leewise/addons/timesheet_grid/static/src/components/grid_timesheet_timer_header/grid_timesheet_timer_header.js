/** @leewise-module **/

import { _t } from "@web/core/l10n/translation";
import { Domain } from "@web/core/domain";
import { useService } from "@web/core/utils/hooks";
import { Record } from "@web/model/record";
import { getRawValue } from "@web/views/kanban/kanban_record";

import { TimesheetTimerHeader } from "../timesheet_timer_header/timesheet_timer_header";

import { Component, onWillStart } from "@leewise/owl";

export class GridTimesheetTimerHeader extends Component {
    static components = {
        TimesheetTimerHeader,
        Record,
    };
    static props = {
        stepTimer: Number,
        timerRunning: Boolean,
        addTimeMode: Boolean,
        headerReadonly: { type: Boolean, optional: true },
        model: Object,
        resId: { type: Number, optional: true },
        updateTimesheet: Function,
        onTimerStarted: Function,
        onTimerStopped: Function,
        onTimerUnlinked: Function,
    };
    static template = "timesheet_grid.GridTimesheetTimerHeader";

    setup() {
        this.notificationService = useService("notification");
        this.timesheetUOMService = useService("timesheet_uom");
        this.timerService = useService("timer");
        onWillStart(this.onWillStart);
    }

    async onWillStart() {
        if (!this.props.model.timerFieldsInfo) {
            await this.props.model.fetchTimerHeaderFields(this.fieldNames);
        }
    }

    get fields() {
        return this.props.model.timerFieldsInfo;
    }

    get fieldNames() {
        return ["name", "project_id", "task_id", "company_id", "timer_start", "unit_amount"];
    }

    getFieldInfo(fieldName) {
        const field = this.fields[fieldName];
        const fieldInfo = {
            attrs: {},
            options: {},
            domain: field.domain || "[]",
            placeholder: field.string || "",
            required: "False",
        };
        if (fieldName === "project_id") {
            if (field.domain) {
                fieldInfo.domain = Domain.and([
                    field.domain,
                    [["timesheet_encode_uom_id", "=", this.timesheetUOMService.timesheetUOMId]],
                ]).toString();
            } else {
                fieldInfo.domain = [
                    ["allow_timesheets", "=", true],
                    ["timesheet_encode_uom_id", "=", this.timesheetUOMService.timesheetUOMId],
                ];
            }
            fieldInfo.context = `{'search_default_my_projects': True}`;
            fieldInfo.required = "True";
        } else if (fieldName === "task_id") {
            fieldInfo.context = `{'default_project_id': project_id, 'search_default_my_tasks': True, 'search_default_open_tasks': True}`;
        } else if (fieldName === "name") {
            fieldInfo.placeholder = _t("Describe your activity...");
        }
        if (field.depends?.length) {
            fieldInfo.onChange = true;
        }
        return fieldInfo;
    }

    get activeFields() {
        const activeFields = {};
        for (const fieldName of this.fieldNames) {
            activeFields[fieldName] = this.getFieldInfo(fieldName);
        }
        return activeFields;
    }

    async onTimesheetChanged(timesheet, changes) {
        const secondsElapsed = this.timerService.toSeconds;
        if (timesheet.isNew) {
            if (changes.project_id || changes.task_id) {
                // create the timesheet when the project is set
                timesheet.save({ reload: false }).then(() => {
                    this.props.updateTimesheet({...Object.fromEntries(
                                this.fieldNames.map((f) => [f, getRawValue(timesheet, f)])
                            ),
                            id: timesheet.resId,
                        },
                        secondsElapsed
                    );
                });
            }
            // Nothing to do since because a timesheet cannot be created without a project set or it is not a manual change.
            return;
        }
        if (
            changes.name === "" &&
            Object.keys(changes).length === 1 &&
            ((!("name" in this.props.model.data.timer) &&
                this.props.model.data.timer.description === "/") ||
                this.props.model.data.timer.name === "/")
        ) {
            return; // nothing to do
        }
        timesheet.save({ reload: false }); // create the timesheet when the project is set
        this.props.updateTimesheet(
            Object.fromEntries(this.fieldNames.map((f) => [f, getRawValue(timesheet, f)]))
        );
    }
}
