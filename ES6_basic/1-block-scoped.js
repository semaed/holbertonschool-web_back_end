export default function taskBlock(trueOrFalse) {
    let task = false; // Use let instead of var
    let task2 = true; // Use let instead of var
  
    if (trueOrFalse) {
      task = true; // No need for var here
      task2 = false; // No need for var here
    }
  
    return [task, task2];
  }
  