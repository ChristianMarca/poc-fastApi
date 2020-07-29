const fs = require('fs');
const lineReader = require('readline').createInterface({
    input: fs.createReadStream('stats.txt')
});
const logger = fs.createWriteStream('log.txt', {
    flags: 'a'
})



let lineNumber = 1;

lineReader.on('line', function (line) {
    if (lineNumber === 2){
        logger.write(line + '\n')
    }
    lineNumber += 1;
    if (lineNumber === 4) {
        lineNumber = 1;
    }
});
