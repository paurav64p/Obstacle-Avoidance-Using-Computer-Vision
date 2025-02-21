# Obstacle-Avoidance-Using-Computer-Vision
An IoT-based edge computing device designed for industrial monitoring. It collects real-time sensor data, processes it locally, and transmits key insights to the cloud for analytics. Features include temperature, humidity, and air quality monitoring, low-power operation, and secure communication.
## Features
- Real-time object detection with **YOLOv4 & Mask R-CNN**
- Sensor fusion with ultrasonic sensors for accurate depth estimation
- Efficient **path-planning algorithms** for obstacle avoidance
- Multi-threaded execution for **low-latency real-time processing**

## Tools & Technologies
- YOLOv4, Mask R-CNN
- OpenCV, NumPy
- TensorFlow/Keras
- Ultrasonic Sensors
- Python, CUDA (optional for acceleration)

## Installation
```sh
# Clone the repository
git clone https://github.com/yourusername/Obstacle-Avoidance-CV.git
cd Obstacle-Avoidance-CV

# Install dependencies
pip install -r requirements.txt

## Future Enhancements
- Implement **depth measurement fusion** for better accuracy
- Optimize **multi-threading** for faster inference
- Use **Reinforcement Learning (RL)** for self-improving obstacle avoidance
