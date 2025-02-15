# Mass Analysis of Moon
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

$$ 
G = (6.6743 \pm 0.00015) \times 10^{-11} \, \text{m}^3 \text{kg}^{-1} \text{s}^{-2} 
$$

Using these values, the Moon’s mass can be calculated with the formula: 

$$ 
\text{Moon’s Mass} = \frac{r \times v^2}{G} 
$$

### Lunar Reconnaissance Orbiter
The Lunar Reconnaissance Orbiter launched on June 18, 2009 to study the Moon and prepare for future human exploration. After reaching the Moon, it began collecting high-resolution data. LRO has mapped the Moon’s surface, studied radiation exposure, identified potential landing sites, and investigated lunar resources like water ice. LRO continues to provide valuable data and it will operate until it runs out of fuel and eventually crashes onto the Moon’s surface. 

LRO SPICE data set contains navigation and related observation geometry and other ancillary data in the form of SPICE System kernel files for the LRO spacecraft. The LRO mission offers detailed measurements of the Moon's gravitational field, topography, and other essential parameters. 

By utilizing this data, we can obtain the necessary orbital parameters to accurately calculate the Moon's mass. 
### SpicePy
SPICE is a software toolkit developed at NASA for investigating planetary and spacecraft positions, as well as ancillary engineering information. It is written in FORTRAN 77 and C. SpiceyPy is a community-developed Python wrapper for SPICE, providing an interface between low-level C functions and higher-level Python, IDL, and MATLAB SPICE wrappers. It is widely used in space missions to manage data related to spacecraft positions, orientations, orbits, and time conversions. NASA extensively utilizes it for precise planetary navigation and trajectory analysis.


### Project Structure

```
OrbitAnalysis-LRO
|
├── kernels
│   ├── meta_kernel.tm    # lists all the kernels to load
|   |
│   ├── lsk               # Directory for Leapseconds kernels.
│   │   ├── lskinfo.txt
│   │   └── naif0012.tls  # Leap second file needed for time conversions.
|   |
│   └── spk               # Directory for SPICE ephemeris kernels.
│       ├── spkinfo.txt
│       └── lrorg_2024167_2024259_v01.bsp 
|     
├── main.py     # Runs the orbit analysis.
└── README.md   # Project documentation.
```

In the SPICE system, **kernels** are specialized files containing data on time conversions, spacecraft trajectories, and celestial positions. The kernels directory providing all the essential data for accurate orbital analysis. Our project organizes these into a few key components:

- **meta_kernel.tm**  
    This master file lists every other kernel we need. Loading it ensures that all relevant data is available for the analysis.
    
- **lsk Folder (Leapseconds Kernels)**  
    Within this folder, the file **naif0012.tls** is critical. It contains the leap second data required to convert human-friendly UTC times into the uniform ephemeris time that SPICE uses, ensuring our time measurements are accurate.
    
- **spk Folder (Spacecraft Ephemeris Kernels)**  
    Here, the file **lrorg_2024167_2024259_v01.bsp** holds the trajectory data for the Lunar Reconnaissance Orbiter. This SPK file provides the positions and velocities needed to determine the spacecraft’s state vector, which is fundamental for calculating orbital parameters.