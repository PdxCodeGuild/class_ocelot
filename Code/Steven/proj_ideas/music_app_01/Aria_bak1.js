// we want -1%4 to be 3, not -1
function mod(a, b) {
    return (a < 0) ? b + a % b : a % b;
}


// new Note('C2')
// new Note('C',2)
// new Note(24)
// new Note(new Note(24))
class Note {
    constructor(a, b) {
        let absolute_index = 0;
        if (typeof a == 'number') {
            absolute_index = a;
        } else if (typeof a == 'string') {
            if (b) {
                absolute_index = Note.absoluteIndexFromRelativeName(a, b);
            } else {
                absolute_index = Note.absoluteIndexFromAbsoluteName(a);
            }
        } else {
            absolute_index = a.absolute_index;
        }
        this.absolute_index = absolute_index;
        this.frequency = 16.352 * Math.pow(2, absolute_index / 12);
    }

    clone() {
        return new Note(this.absolute_index);
    }

    getRelativeIndex() {
        return mod(this.absolute_index, 12);
    }

    getOctave() {
        return Math.floor(this.absolute_index / 12);
    }

    getRelativeName() {
        let relative_index = this.getRelativeIndex();
        return Note.relative_names[relative_index][0];
    }

    getAbsoluteName() {
        let relative_name = this.getRelativeName();
        let octave = this.getOctave();
        return relative_name + octave;
    }
    static absoluteIndexFromAbsoluteName(absolute_name) {
        let relative_name = absolute_name.match(/\D+/)[0];
        let octave = parseInt(absolute_name.match(/\d+/)[0]);
        return Note.absoluteIndexFromRelativeName(relative_name, octave);
    }
    static absoluteIndexFromRelativeName(relative_name, octave) {
        for (let i=0; i<Note.relative_names.length; ++i) {
            for (let j=0; j<Note.relative_names[i].length; ++j) {
                if (Note.relative_names[i][j] === relative_name) {
                    return 12*octave + i;
                }
            }
        }
        return null;
    }
}

// uses # and b instead of ♯ and ♭
Note.relative_names = [['C'],
    ['C#/Db', 'C#', 'Db'],
    ['D'],
    ['D#/Eb', 'D#', 'Eb'],
    ['E'],
    ['F'],
    ['F#/Gb', 'F#', 'Gb'],
    ['G'],
    ['G#/Ab', 'G#', 'Ab'],
    ['A'],
    ['A#/Bb', 'A#', 'Bb'],
    ['B']];




class Scale {
    // key: either a string containing the absolute name, or the note itself
    // pattern: either a string containing the name of the pattern, or an array of ints
    constructor(key, pattern) {
        if (typeof key == 'string') {
            key = new Note(key);
        }
        this.key = key;

        if (typeof pattern == 'string') {
            pattern = Scale.patterns[pattern];
        }
        this.pattern = pattern;
    }

    // to make look-up more efficient, store cumulative, reverse_cumulative, and pattern sums
    getNote(i) {
        let n_half_steps = 0;
        if (i < 0) {
            for (let k=0; k>i; --k) {
                n_half_steps -= this.pattern[mod(k, this.pattern.length)];
            }
        } else {
            for (let k=0; k<i; ++k) {
                n_half_steps += this.pattern[mod(k, this.pattern.length)];
            }
        }
        return new Note(this.key.absolute_index + n_half_steps);
    }
}


Scale.patterns = {
    chromatic: [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    major: [2, 2, 1, 2, 2, 2, 1],
    natural_minor: [2, 1, 2, 2, 1, 2, 2],
    minor_pentatonic: [3, 2, 2, 3, 2],
    blues: [3, 2, 1, 1, 3, 2],
    major_pentatonic: [2, 2, 3, 2, 3],
    harmonic_minor: [2, 1, 2, 2, 1, 3, 2],
    melodic_minor: [2, 1, 2, 2, 2, 2, 1],
    ionian: [2, 2, 1, 2, 2, 2, 1],
    dorian: [2, 1, 2, 2, 2, 1, 2],
    phrygian: [1, 2, 2, 2, 1, 2, 2],
    lydian: [2, 2, 2, 1, 2, 2, 1],
    mixolydian: [2, 2, 1, 2, 2, 1, 2],
    aeolian: [2, 1, 2, 2, 1, 2, 2],
    locrian: [1, 2, 2, 1, 2, 2, 2],
    whole_tone: [2, 2, 2, 2, 2, 2],
    whole_half_diminished: [2, 1, 2, 1, 2, 1, 2, 1],
    half_whole_diminished: [1, 2, 1, 2, 1, 2, 1, 2]
};


class PlayedNote extends Note {
    // new PlayedNote('C2', 0.1)
    // new PlayedNote(new Note('C2'), 0.1)
    constructor(note, duration) {
        super(note);
        this.duration = duration;
    }
}

class Melody {
    // new Melody('C2', 'dorian', [1,0,-1,0,1,2,1], 0.3)
    // new Melody([new PlayedNote('C2', 0.3), new PlayedNote('C3', 0.3)])
    constructor(notes=[]) {
        this.notes = notes;
    }
    getNote(i) {
        return this.notes[i];
    }
    totalNotes() {
        return this.notes.length;
    }
    add(m) {
        for (let i=0; i<m.notes.length; ++i) {
            this.played_notes.push(m.notes[i]);
        }
        return this;
    }
    repeat(n) {
        let original_length = this.notes.length;
        for (let i=1; i<n; ++i) {
            for (let j=0; j<original_length; ++j) {
                this.notes.push(this.notes[j]);
            }
        }
        return this;
    }
    rotate(n) {
        n = mod(n, this.notes.length);
        let lower = this.notes.slice(this.notes.length - n);
        let upper = this.notes.slice(0, this.notes.length - n);
        this.notes = lower.concat(upper);
        return this;
    }
    getNoteNames() {
        let names = [];
        for (let i=0; i<this.notes.length; ++i) {
            names.push(this.notes[i].getAbsoluteName());
        }
        return names;
    }
    clone() {
        let notes = [];
        for (let i=0; i<notes.length; ++i) {
            notes.push(this.notes[i].clone());
        }
        return new Melody(notes);
    }
}

class GeneratedMelody extends Melody {
    constructor(key, scale_name, pattern, duration) {
        super([]);
        this.key = key;
        this.scale_name = scale_name;
        this.pattern = pattern;
        this.duration = duration;
        let scale = new Scale(key, scale_name);
        for (let i=0; i<pattern.length; ++i) {
            this.notes.push(new PlayedNote(scale.getNote(pattern[i]), duration));
        }
    }
    clone() {
        return new GeneratedMelody(this.key, this.scale_name, this.pattern, this.duration);
    }
}


function random_pattern(low, high, n) {
    let pattern = [];
    for (let i=0; i<n; ++i) {
        let value = low + Math.floor(Math.random()*(high-low+1));
        pattern.push(value);
    }
    return pattern;
}








let select_scale = document.querySelector('#select_scale');
let key_input = document.querySelector('#key_input');
let duration_input = document.querySelector('#duration_input');
let delay_input = document.querySelector('#delay_input');
let melody_input = document.querySelector('#melody_input');
let play_bt = document.querySelector('#play_bt');
let stop_bt = document.querySelector('#stop_bt');

let lower_bound_input = document.querySelector('#lower_bound_input');
let upper_bound_input = document.querySelector('#upper_bound_input');
let n_notes_input = document.querySelector('#n_notes_input');
let generate_bt = document.querySelector('#generate_bt');

for (scale_name in Scale.patterns) {
    let option = document.createElement('option');
    option.innerText = scale_name;
    option.setAttribute('value', scale_name);
    select_scale.appendChild(option);
}


let play_interval = null;

play_bt.onclick = function() {
    let scale_name = select_scale.options[select_scale.selectedIndex].value;
    let key = key_input.value;
    let duration = parseFloat(duration_input.value);
    let delay = parseFloat(delay_input.value);
    let pattern = melody_input.value.split(/[^\d-]/);
    pattern = pattern.filter((x) => x.length > 0);
    for (let i=0; i<pattern.length; ++i) {
        pattern[i] = parseInt(pattern[i]);
    }
    let melody = new GeneratedMelody(key, scale_name, pattern, duration);
    console.log(melody.getNoteNames());
    melody.repeat(4);

    let synth = new Tone.Synth().toMaster();
    let note_position = 0;
    play_interval = setInterval(function(){
        let played_note = melody.getNote(note_position);
        synth.triggerAttackRelease(played_note.frequency, played_note.duration);
        note_position = (note_position+1)%melody.totalNotes();
    }, delay*1000);
    play_bt.style.display = 'none';
    stop_bt.style.display = '';
}


stop_bt.onclick = function() {
    if (play_interval) {
        clearInterval(play_interval);
    }
    play_bt.style.display = '';
    stop_bt.style.display = 'none';
}

function restartPlay() {
    if (play_interval) {
        stop_bt.onclick();
        play_bt.onclick();
    }
}

generate_bt.onclick = function() {
    let lower_bound = parseInt(lower_bound_input.value);
    let upper_bound = parseInt(upper_bound_input.value);
    let n_notes = parseInt(n_notes_input.value);
    melody_input.value = random_pattern(lower_bound, upper_bound, n_notes).join(', ');
    restartPlay();
}



select_scale.onchange = restartPlay;
key_input.onchange = restartPlay;
duration_input.onchange = restartPlay;
delay_input.onchange = restartPlay;
melody_input.onchange = restartPlay;

select_scale.value = 'dorian';
key_input.value = 'C2';
duration_input.value = 0.1;
delay_input.value = 0.3;
lower_bound_input.value = -5;
upper_bound_input.value = 5;
n_notes_input.value = 6;
stop_bt.style.display = 'none';
melody_input.value = '5, -5, -5, 4, -4, -1';
//generate_bt.onclick();






