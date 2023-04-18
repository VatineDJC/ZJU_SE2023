import {reactive} from "vue";

export const global_data = reactive({
    cur_nav: 0,
    light_list: {},
    lock_list: {},
    sensor_list: {},
    switch_list: {}
})

export function isObjectEmpty(obj) {
    for (let i in obj)
        return false;
    return true;
}