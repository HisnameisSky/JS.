function steamrollArray(arr) {
  const flattened = [];

  function flatten(item) {
    if (Array.isArray(item)) {
      // 
      for (let i = 0; i < item.length; i++) {
        flatten(item[i]);
      }
    } else {
      flattened.push(item);
    }
  }

  for (let i = 0; i < arr.length; i++) {
    flatten(arr[i]);
  }

  return flattened;
}

//alt

function stramrollArray(arr) {
    return arr.reduce((acc, val) => {
        return acc.concat(Array.isArray(val)? stramrollArray(val): val);
    }, []);
}

//

function streamrollArrayStack(arr){
  const stack = [...arr];
  const result = [];
  while(stack.length > 0){
    const next = stack.pop();

    if(Array.isArray(next)){
      stack.push(...next);
    } else{
      result.push(next);
    }
  }
  return result;
}

console.log(streamrollArrayStack([1,{},[3,[[4]]]]));

//


import readline from 'readline';
import fs from 'fs';

const rl = readline.createInterface({ input: fs.createReadStream('hug_file.txt')});
rl.on('line',(line)=> {
  //O(1);
});

/* node --max-old-space-size-8192 app.js */

//

import fs from 'node.fs';
import { pipeline } from 'node:stream/promises';
import { Transform } from 'node:stream';
import realine from 'node:readline';

const filterStream = new Transform({
  transform(chunk, encoding, callback) {
    const line = chunk.toString();

    if (line.includes('ERROR')){
      this.push(line + '\n');
    }
    callback();
  }
});

async function processHugeFile(){
  try {
    await pipeline(
      fs.createReadStream('input_huge_log.txt'),
      filterStream,
      fs.createWriteStream('output_errors.txt')
    );

  console.log('処理が正常に完了しました。');  
  } catch {
  console.error('ストリーム処理中にエラーが発生しました:', err);
  }
}

//

import fs from 'node:fs';
import { pipeline } from 'node:strea/promises';

async function* transformData(source){
  for await (const chunk of source) {
    const text= chunk.toString().toUpperCase();
    yield text;
  }
}

async function run() {
  try {
    await pipeline(
      fs.createReadStream('large_file.txt'),
      transformData,
      fs.createWriteStream('transformed_file.txt')
    );
    cconsole.log('パイプライン処理成功！');
  } catch (err) {
    console.error('処理失敗:', err);
  }
}

run();