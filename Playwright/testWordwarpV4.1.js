function wrapText(input, maxLines, width) {
  // 移除 CR 並清理行尾空白
  input = input.replace(/\r/g, '').replace(/[ \t]+$/gm, '');

  const lines = input.split('\n');
  const resultLines = [];

  // 文字換行的封裝函數
  const wrapLine = (text, width) => {
    const words = text.trim().split(/\s+/);
    const wrapped = [];
    let current = '';

    for (const word of words) {
      if (word.length > width) {
        if (current) {
          wrapped.push(current);
          current = '';
        }
        for (let i = 0; i < word.length; i += width) {
          wrapped.push(word.slice(i, i + width));
        }
      } else {
        if ((current + (current ? ' ' : '') + word).length <= width) {
          current += (current ? ' ' : '') + word;
        } else {
          wrapped.push(current);
          current = word;
        }
      }
    }

    if (current) wrapped.push(current);
    return wrapped;
  };

  // 對每行進行處理（含空白行）
  for (const line of lines) {
    const trimmed = line.trim();
    if (trimmed === '') {
      resultLines.push('');
    } else {
      resultLines.push(...wrapLine(trimmed, width));
    }
  }

  // 移除末尾多餘空白行
  while (resultLines.length && resultLines[resultLines.length - 1] === '') {
    resultLines.pop();
  }

  // 輸出組裝
  const finalOutput = resultLines.map((line, i) =>
    i < resultLines.length - 1 ? line + '\n' : line
  ).join('');

  // 計算長度：sum of line lengths + 2 * (lines - 1)
  const totalTextLength = resultLines.reduce((sum, line) => sum + line.length, 0);
  const totalLength = totalTextLength + (resultLines.length > 1 ? 2 * (resultLines.length - 1) : 0);
  const maxAllowedLength = maxLines * width + 2 * (maxLines - 1);

  const isValidLength = totalLength <= maxAllowedLength;
  const isValidLines = resultLines.length <= maxLines;

  return {
    output: finalOutput,
    isValid: isValidLength && isValidLines,
    linesUsed: resultLines.length,
    totalLength,
    maxAllowedLength
  };
}

const maxLines = 3;
const width = 10;

const successCases = [
  "12\n\n34",     // 3 lines: "12", "", "34" → 2+0+2 + (3-1)*2 = 8
  "1234567890",   // 1 line, exactly width 10 → 10
  "12 34 56",     // 1 line: 8 chars + 0
  "12\n34",       // 2 lines → 2+2 + 2 = 6
  "a b c d e f g h i j",
  "123456789012345678901",        // 3 lines: 25 chars
  "123456789012345678901234567890",// 10+10+10 = 30 + 4 = 34 → max ok
  "line1\n\n\n\n",                  // 5 lines = too many
  "wordword\nwordword",  
  "1234567890".repeat(3),
  "123\n4567890\n1234567890    \n\n",
  "12\n34\n56",
  "1234567890123",
  "1".repeat(30),
  "1".repeat(29),
  "abcdefgh\nijklmnopqrstuvwxyz", 
  "12345678901234567890\n1234567890", 
  "hi world a wrap test w 3 lines",    
];

const failCases = [

  "12\n\n\n34",                   // 4 lines → exceeds maxLines = 3
  "12\n".repeat(5),               // 5 lines → 5*2 + 4*2 = 18
  "12345678 901234 567890\n1234567890", 
  "hi world a wrap testing w 3", 
  "1234567890123456789012345678901",  
  "abc def ghi jkl mno pqr stu vwx yz",
  "abcdefghij\nabcdefghij\nabcdefghijdd",
  "abcdefgh\nijklmno\nstuvwxyzdddd",    
  "1".repeat(32),
  "abcdefghij\nabcdefghij\nabcdefghij\nx",
  "12345678901".repeat(3),
  "12345678901234567890\n12345678901234567890",
  "✅ **使用者需求說 明：wrapText 函數**"  
];

console.log(`Max Lines: ${maxLines}, Width: ${width}, Max Allowed Length: ${maxLines * width + 2 * (maxLines - 1)}\n\n`);
console.log("✅ SUCCESS CASES:\n");
successCases.forEach((test, idx) => {
  const res = wrapText(test, maxLines, width);
  console.log(`Test ${idx + 1}: ${res.isValid ? "PASS" : "FAIL"}`);
  console.log(res.output);
  console.log(`\nLines used: ${res.linesUsed}, Total length: ${res.totalLength}\n`);
  console.log("---");
});

console.log("\n❌ FAILURE CASES:\n");
failCases.forEach((test, idx) => {
  const res = wrapText(test, maxLines, width);
  console.log(`Test ${idx + 1}: ${!res.isValid ? "FAILED" : "UNEXPECTED PASS"}`);
  console.log(res.output);
  console.log(`\nLines used: ${res.linesUsed}, Total length: ${res.totalLength}\n`);
  console.log("---");
});
