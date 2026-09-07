# Write your simp_alert function and three calls here
// 1. Define the simp_alert function with its five tracking parameters
function simp_alert(money_spent, texts_sent, texts_replied, dates_asked, dates_accepted) {
 
// 2. Perform the individual rate calculations
    const reply_rate = texts_replied / texts_sent;
    const date_rate = dates_accepted / dates_asked;
    
 // 3. Compute the global composite balance score
    const score = (reply_rate + date_rate) / 2;
    
 // 4. Apply the strict threshold rules logic
    if (score >= 0.5) {
        return "She likes you";
    } else if (score >= 0.2) {
        return "Lukewarm";
    } else {
        return "You are simping";
    }
}

// 5. Call the function three times in the required order and log the results
console.log(simp_alert(45000, 80, 2, 10, 0));
console.log(simp_alert(8000, 20, 15, 4, 2));
console.log(simp_alert(18000, 20, 6, 5, 1));