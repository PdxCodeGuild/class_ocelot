// Timer function

var input_timer = document.getElementById('input_timer');
var bt_start_timer = document.getElementById('bt_start_timer');
var view_timer = document.getElementById('view_timer');

var timer_date = null;
var timer_interval = null;

bt_start_timer.onclick = function() {
    timer_date = new Date();
    timer_date.setHours(0, 5, 0, 0);
    timer_interval = setInterval(update_timer, 1000);
    view_timer.innerHTML = time_str(timer_date);
};

function update_timer() {
    timer_date.setSeconds(timer_date.getSeconds()-1);
    view_timer.innerHTML = time_str(timer_date);
    if (timer_date.getSeconds() === 0
        && timer_date.getMinutes() === 0
        && timer_date.getHours() === 0) {
        clearInterval(timer_interval);
        timer_interval = null;