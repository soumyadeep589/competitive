console.log('Start');

process.nextTick(() => {
  console.log('Next Tick 1');
});

new Promise((resolve) => {
  console.log('Promise 1');
  resolve();
}).then(() => {
  console.log('Promise Callback 1');
  queueMicrotask(() => {
    console.log('Microtask 1');
  });
});

queueMicrotask(() => {
  console.log('Microtask 2');
});

process.nextTick(() => {
  console.log('Next Tick 2');
});

console.log('End');

//------------------------------------------------------------------------------



// setTimeout(function timeout () {
//     console.log("timeout");
//    },0);
// setImmediate(function immediate () {
//     console.log("immediate");
//    });


//------------------------------------------------------------------------------


// queueMicrotask(() => {
//     console.log('This will be logged first.');
//   });
  
//   process.nextTick(() => {
//     console.log('This will be logged second.');
//   });


//------------------------------------------------------------------------------


// function task1() {
//     console.log('promise1 resolved');
// }

// function task2() {
//     console.log('promise2 resolved');
//     process.nextTick(task10);
// }

// function task3() {
//     console.log('promise3 resolved');
// }

// function task4() {
//     console.log('immediate 1');
// }

// function task5() {
//     console.log('tick 1');
// }

// function task6() {
//     console.log('tick 2');
// }

// function task7() {
//     console.log('microtask 1');
// }


// function task8() {
//     console.log('timeout');
// }


// function task9() {
//     console.log('immediate 2');
// }

// function task10() {
//     console.log('tick3');
//     queueMicrotask(task11);
// }

// function task11() {
//     console.log('microtask 2');
// }

// Promise.resolve().then(task1);
// Promise.resolve().then(task2);

// Promise.resolve().then(task3);

// setImmediate(task4);

// process.nextTick(task5);
// process.nextTick(task6);

// queueMicrotask(task7);

// setTimeout(task8, 0);

// setImmediate(task9);

//------------------------------------------------------------------------------
