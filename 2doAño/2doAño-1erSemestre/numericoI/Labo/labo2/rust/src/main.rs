fn main() {
    rnewton(ej3labo, -20.0, 10.0e-4, 50);
}

fn rnewton(f: fn(f64) -> (f64, f64), mut x_0: f64, err: f64, mit: i32) -> (Vec<f64>, Vec<f64>) {
    let mut ev_f = f(x_0).0;
    let mut ev_fp = f(x_0).1;
    let mut x_1: f64;
    let mut hf: Vec<f64> = Vec::new();
    let mut hx: Vec<f64> = Vec::new();
    hf.push(ev_f);
    hx.push(x_0);

    if ev_f.abs() < err {
        println!("Arrancaste ya con algo cercano a la raiz");
        return (hf, hx);
    };
    for _n in 1..mit {
        x_1 = x_0 - ev_f / ev_fp;
        ev_f = f(x_1).0;
        ev_fp = f(x_1).1;
        x_0 = x_1;

        hf.push(ev_f);
        hx.push(x_0);
        if ev_f.abs() < err {
            println!("Bounded error reached");
            println!("La raiz es {}, el error {}", x_0, ev_f);
            return (hf, hx);
        }
    }
    println!("Max iteration reached");
    println!("La raiz es {}, el error {}", x_0, ev_f);
    return (hf, hx);
}

fn ej3labo(x: f64) -> (f64, f64) {
    return (f64::powf(x, 3.0) - 8.0, 3.0 * f64::powf(x, 2.0));
}
