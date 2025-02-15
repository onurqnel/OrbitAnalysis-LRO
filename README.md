# Weight Analysis of Moon

### Introduction
The Lunar Reconnaissance Orbiter launched on June 18, 2009 to study the Moon and prepare for future human exploration. After reaching the Moon, it began collecting high-resolution data. LRO has mapped the Moon’s surface, studied radiation exposure, identified potential landing sites, and investigated lunar resources like water ice. LRO continues to provide valuable data and it will operate until it runs out of fuel and eventually crashes onto the Moon’s surface. 

SPICEPy is the Python interface for NASA's SPICE Toolkit, which is used for space missions to handle data related to spacecraft positions, orientations, orbits, and time conversions. It is widely used in NASA's space missions for precise calculations related to planetary navigation and trajectory analysis. 

LRO SPICE data set contains navigation and related observation geometry and other ancillary data in the form of SPICE System kernel files for the LRO spacecraft. The LRO mission offers detailed measurements of the Moon's gravitational field, topography, and other essential parameters. 

By utilizing this data, we can obtain the necessary orbital parameters to accurately calculate the Moon's mass. To determine the weight of a planet, we use the formula:

$$ \text{Weight} = \text{Mass} \times \text{Gravitational Acceleration} $$

There are several methods for estimating the mass of a planet, but the most precise calculations rely several approaches
##### Using Natural Satellites  
If a planet has natural satellites, its mass can be determined using Newton's law of universal gravitation. By applying a generalized form of Kepler’s third law, which accounts for both the planet's and the moon’s mass, we can derive an accurate estimate.
##### Data from Spacecrafts
Observations of spacecrafts around a planet provide highly accurate method for mass estimation. By analyzing the spacecraft's motion and the gravitational influence exerted by the planet, we can determine its mass with great precision.

### Determining the Moon’s Mas
I will determine the Moon’s mass based on spacecraft orbiting it. This method is highly precise and relatively simple. To calculate the Moon’s mass, we need the following data:

- **Orbital Radius (r):** The distance from the center of the Moon to the orbiting object.  

- **Orbital Speed (v):** The speed at which an object orbits the Moon.  

- **Gravitational Constant (G):**
$$ G = (6.6743 \pm 0.00015) \times 10^{-11} \, \text{m}^3 \text{kg}^{-1} \text{s}^{-2} $$

Using these values, the Moon’s mass can be calculated with the formula:
$$ \text{Moon’s Mass} = \frac{r \times v^2}{G} $$

### Kernels







```
OrbitAnalysis-LRO
├── kernels
│   ├── fk
│   │   ├── fkinfo.txt
│   │   ├── moon_080317.lbl
│   │   ├── moon_080317.tf
│   │   ├── moon_assoc_me.lbl
│   │   ├── moon_assoc_me.tf
│   │   ├── moon_assoc_pa.lbl
│   │   └── moon_assoc_pa.tf
│   ├── lsk
│   │   ├── lskinfo.txt
│   │   ├── naif0012.lbl
│   │   └── naif0012.tls
│   ├── meta_kernel.tm
│   ├── pck
│   │   ├── pck00010.lbl
│   │   ├── pck00010.tpc
│   │   └── pckinfo.txt
│   ├── sclk
│   │   ├── lro_clkcor_2024262_v00.lbl
│   │   ├── lro_clkcor_2024262_v00.tsc
│   │   └── sclkinfo.txt
│   └── spk
│       ├── lrorg_2024167_2024259_v01.bsp
│       ├── lrorg_2024167_2024259_v01.lbl
│       └── spkinfo.txt
├── main.py
└── README.md
```
