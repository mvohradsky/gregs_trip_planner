/** @odoo-module **/

import { CalendarRenderer } from "@web/views/calendar/calendar_renderer";
import { useService } from "@web/core/utils/hooks";
import { registry } from "@web/core/registry";
import { Component, useState } from "@odoo/owl";

class TripCalendarRenderer extends CalendarRenderer {

    setup() {
        super.setup();
        this.orm = useService("orm");
        this.notification = useService("notification");
        this.state = useState({ draggingTask: null });
    }

    async onDropTask(event, date) {
        const taskId = this.state.draggingTask;
        if (!taskId) return;

        try {
            const res = await this.orm.call("gregs.service_trip", "create_trip_from_task", [taskId, date]);
            if (res) {
                this.notification.add("Výjezd úspěšně naplánován.", { type: "success" });
                this.trigger("reload");
            }
        } catch (error) {
            this.notification.add("Nepodařilo se naplánovat výjezd.", { type: "danger" });
        } finally {
            this.state.draggingTask = null;
        }
    }

    onDragStartTask(taskId) {
        this.state.draggingTask = taskId;
    }

}

registry.category("views").add("trip_calendar_renderer", TripCalendarRenderer);
