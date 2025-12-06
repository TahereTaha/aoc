
function rotate_dial(dial, instruction) {
	let direction;
	if (instruction[0] == 'L') {
		direction = 'left';
	}
	else if (instruction[0] == 'R') {
		direction = 'right';
	}
	let passes_throug_zero = 0;
	let magnitud = Number(instruction.slice(1, instruction.length));
	while (magnitud != 0)
	{
		if (direction == 'left') {
			dial--;
		}
		else if (direction == 'right') {
			dial++;
		}
		if (dial == 100) {
			dial = 0
		}
		else if (dial == -1) {
			dial = 99
		}
		if (dial == 0) {
			passes_throug_zero++;
		}
		magnitud--;
	}
	return [dial, passes_throug_zero];
}

const fs = require('node:fs');

const file_text = fs.readFileSync('input', 'utf8');

const lines = file_text.split("\n");

let dial = 50;

let acc = 0;

let i = 0;
while (i < lines.length)
{
	if (lines[i].length > 0) {
		let return_data = rotate_dial(dial, lines[i]);
		dial = return_data[0];
		acc += return_data[1];
	}
	i++;
}

console.log(acc);



