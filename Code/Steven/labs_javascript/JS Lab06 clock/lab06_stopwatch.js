// stopwatch -------------------------------------------------------------------------

var get23414 = document.getElementById;



var view_stopwatch = document.getElementById('view_stopwatch');
var bt_start_stopwatch = document.getElementById('bt_start_stopwatch');
var bt_stop_stopwatch = document.getElementById('bt_stop_stopwatch');
var bt_pause_stopwatch = document.getElementById('bt_pause_stopwatch');
var bt_resume_stopwatch = document.getElementById('bt_resume_stopwatch');

var stopwatch_date = null;
var stopwatch_interval = null;

bt_pause_stopwatch.style.display = 'none';
bt_resume_stopwatch.style.display = 'none';
bt_stop_stopwatch.style.display = 'none';

bt_start_stopwatch.onclick = function() {
    stopwatch_date = new Date();
    stopwatch_date.setHours(0, 0, 0, 0);
    stopwatch_interval = setInterval(update_stopwatch, 1000);
    view_stopwatch.innerHTML = time_str(stopwatch_date);
    bt_start_stopwatch.style.display = 'none';
    bt_pause_stopwatch.style.display = 'initial';
    bt_stop_stopwatch.style.display = 'initial';
};
bt_stop_stopwatch.onclick = function() {
    clearInterval(stopwatch_interval);
    stopwatch_interval = null;
    stopwatch_date = new Date();
    stopwatch_date.setHours(0, 0, 0, 0);
    view_stopwatch.innerHTML = time_str(stopwatch_date);
    bt_start_stopwatch.style.display = 'initial';
    bt_resume_stopwatch.style.display = 'none';
    bt_pause_stopwatch.style.display = 'none';
    bt_stop_stopwatch.style.display = 'none';
};
bt_pause_stopwatch.onclick = function() {
    clearInterval(stopwatch_interval);
    stopwatch_interval = null;
    bt_resume_stopwatch.style.display = 'initial';
    bt_pause_stopwatch.style.display = 'none';
};
bt_resume_stopwatch.onclick = function() {
    stopwatch_interval = setInterval(update_stopwatch, 1000);
    bt_resume_stopwatch.style.display = 'none';
    bt_pause_stopwatch.style.display = 'initial';

};

function update_stopwatch() {
    stopwatch_date.setSeconds(stopwatch_date.getSeconds()+1);
    view_stopwatch.innerHTML = time_str(stopwatch_date);
}



