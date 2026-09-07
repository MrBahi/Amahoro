console.log("============ EXERCISE 1 ========")
// Function definitions
function greetUser(name) {
    return `Welcome, ${name}! Ready to build?`;
}

// Executing the required sample logs
console.log(greetUser("Amerix"));
console.log(greetUser("SMP Member"));

console.log("\n========== EXERCISE 2 =========")
// Paste the weeks array above, loop through it, and print the report

const weeks = [
  { amount_spent: 8000,  texts_sent: 40, texts_replied: 2 },
  { amount_spent: 12000, texts_sent: 55, texts_replied: 3 },
  { amount_spent: 9000,  texts_sent: 38, texts_replied: 4 },
  { amount_spent: 11000, texts_sent: 42, texts_replied: 2 },
  { amount_spent: 12000, texts_sent: 35, texts_replied: 3 },
];

// 1. Initialize tracker variables
let totalSpent = 0;
let totalSent = 0;
let totalReplies = 0;

// 2. Loop through each week record row
for (const week of weeks) {
  totalSpent += week.amount_spent;
  totalSent += week.texts_sent;
  totalReplies += week.texts_replied;
}

// 3. Compute the reply rate percentage (rounded to nearest whole number)
const replyRate = Math.round((totalReplies / totalSent) * 100);

// 4. Print the final dashboard tracking summary report
console.log(`Total spent: KES ${totalSpent}`);
console.log(`Texts sent: ${totalSent}`);
console.log(`Replies received: ${totalReplies}`);
console.log(`Reply rate: ${replyRate}%`);
console.log(`Verdict: Cut your losses`);
