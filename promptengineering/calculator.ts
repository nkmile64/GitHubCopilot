class Calc{
    add(a: number, b: number): number {
        // log the result of the addition
        console.log('The result of the addition is: ' + (a + b));
        return a + b;
    }

    subtract(a: number, b: number): number {
        return a - b;
    }

    fibonacci(n: number): number {
        if (n <= 1) return n;
        let prev = 0, curr = 1;
        for (let i = 2; i <= n; i++) {
            [prev, curr] = [curr, prev + curr];
        }
        return curr;
    }
}

let calculator = new Calc();
calculator.add(5, 10);