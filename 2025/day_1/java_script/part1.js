
function rotate_dial(dial, instruction) {
	let direction;
	if (instruction[0] == 'L') {
		direction = 'left';
	}
	else if (instruction[0] == 'R') {
		direction = 'right';
	}
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
		magnitud--;
	}
	return dial;
}

const fs = require('node:fs');

const file_text = fs.readFileSync('input', 'utf8');

const lines = file_text.split("\n");

let dial = 50;

let acc = 0;

let i = 0;
while (i < lines.length)
{
	dial = rotate_dial(dial, lines[i]);
	if (dial == 0) {
		acc++;
	}
	i++;
}

console.log(acc);



