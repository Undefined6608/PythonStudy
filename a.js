let arr = [
  {
    totalRadiation: 24.88,
    useHours: 1.4431889957189976,
    datetime: "2024-05-01",
    station: "新胜天泰光伏电站",
    maxpower: 73.69,
    maxtime: "2024-05-01 09:05:00",
    minpower: 0.05,
    mintime: "2024-05-01 18:55:00",
    maxNormalPower: 73.49,
    maxNormalPowerTime: "2024-05-01 09:05:00",
    power: 205.64,
    theoryPower: 913.63,
    time: 12.75,
    temp: 17.3,
    wind: 1.29,
    averageIrradiance: 333.47,
    irradiance: 8003.31,
    maxIrradiance: 0,
  },
];

let arr1 = arr.map(item=>Object.keys(item).map(key=>item[key]?item[key]:"--"));
console.log(arr1)
