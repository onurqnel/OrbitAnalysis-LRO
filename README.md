There are several methods for estimating the mass of a planet, but the most precise calculations rely upon several approaches

##### 1. Using Natural Satellites  
If a planet has natural satellites, its mass can be determined using Newton's law of universal gravitation. By applying a generalized form of Kepler’s third law, which accounts for both the planet's and the moon’s mass, we can derive an accurate estimate.

##### 2. Data from Spacecrafts
Observations of spacecraft around a planet provide a highly accurate method for mass estimation. By analyzing the spacecraft's motion and the gravitational influence exerted by the planet, we can determine its mass with great precision.

### Determining Moon’s Mas
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

LRO SPICE data set contains navigation and related observation geometry and other ancillary data in the form of SPICE System kernel files for the LRO spacecraft. The LRO mission offers detailed measurements of the Moon's gravitational field, topography, and other essential parameters.By utilizing this data, we can obtain the necessary orbital parameters to accurately calculate the Moon's mass. 

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

In the SPICE system, **kernels** are specialized files containing data on time conversions, spacecraft trajectories, and celestial positions. The kernels directory providing all the essential data for accurate orbital analysis. 

- **meta_kernel.tm**  
    This master file lists every other kernel we need. Loading it ensures that all relevant data is available for the analysis.
    
- **lsk Folder (Leapseconds Kernels)**  
    Within this folder, the file **naif0012.tls** is critical. It contains the leap second data required to convert human-friendly UTC times into the uniform ephemeris time that SPICE uses, ensuring our time measurements are accurate.
    
- **spk Folder (Spacecraft Ephemeris Kernels)**  
    Here, the file **lrorg_2024167_2024259_v01.bsp** holds the trajectory data for the Lunar Reconnaissance Orbiter. This SPK file provides the positions and velocities needed to determine the spacecraft’s state vector, which is fundamental for calculating orbital parameters.

### Output

```
(venv) archlinux% python main.py 
Ephemeris time for 2024-06-20T00:00:00 is: 772113669.1844125
Orbital radius (r): 1850335.11 m
Orbital speed (v): 1617.86 m/s
Calculated Moon's mass: 7.256e+22 kg
```

### Overall Error
The estimated mass of the Moon is very close to the widely accepted value of **7.34 × 10²² kg**. Our calculation gives a result that is about **1.24% difference**. This small difference is due to assumptions in our calculation. We used a simplified formula and assumed the Moon follows a perfectly circular orbit based on a single moment in time. In reality, the Moon's orbit is slightly elliptical and influenced by other factors, leading to minor variations in the computed mass.

### Results
Hypothetically, if we placed the Moon on Earth, we could calculate its weight using Earth's gravity. 

$$
\text{Moon Weight} = \text{Moon Mass} \times \text{Earth Gravity}
$$

$$
\approx (7.35 \times 10^{22} \text{ kg}) \times (9.81 \text{ m/s}^2)
$$

$$
\approx 7.21 \times 10^{23} \text{ N}
$$

if we calculate its weight using the Moon’s own gravity:

$$
g_{\text{Moon}} = 1.625 \text{ m/s}^2
$$

$$
\text{Weight on Moon} = (7.35 \times 10^{22} \text{ kg}) \times (1.625 \text{ m/s}^2)
$$

$$
\approx 1.19 \times 10^{23} \text{ N}
$$

### Conclusion
Using spacecraft data and gravity laws can accurately estimate a planet's mass. By applying SPICE and SpicePy tools to obtain orbital parameters, calculating the Moon’s mass to be very close to the accepted value. Despite small simplifications, this approach provides effective for understanding planetary masses and highlights the importance of precise data and analysis in space research.

### References
1. NASA. _Lunar Reconnaissance Orbiter (LRO)_. from [https://science.nasa.gov/mission/lro/](https://science.nasa.gov/mission/lro/
2. NASA Navigation and Ancillary Information Facility (NAIF). _LRO SPICE Kernels – PDS Data Set_, from [https://naif.jpl.nasa.gov/pub/naif/pds/data/lro-l-spice-6-v1.0/lrosp_1000/aareadme.htm](https://naif.jpl.nasa.gov/pub/naif/pds/data/lro-l-spice-6-v1.0/lrosp_1000/aareadme.htm)
3. Annex, A., Ringuette, J., Acton, C., Barrett, J., Deen, R., Hughes, J. A., … & Sides, S. (2020). SpiceyPy: A Pythonic wrapper for the SPICE toolkit. _Journal of Open Source Software, 5_(50), 2050. [https://doi.org/10.21105/joss.02050](https://doi.org/10.21105/joss.02050)
4. Wikipedia contributors. _Planetary mass_. Wikipedia, The Free Encyclopedia. Retrieved February 15, 2025, from [https://en.wikipedia.org/wiki/Planetary_mass](https://en.wikipedia.org/wiki/Planetary_mass)
