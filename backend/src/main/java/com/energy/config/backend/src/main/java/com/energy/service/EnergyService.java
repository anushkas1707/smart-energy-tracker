@Service
public class EnergyService {
    @Autowired
    private EnergyRepository repository;

    public void processSensorData(SensorData data) {
        // Store in InfluxDB
        repository.save(data);
        
        // Check for anomalies
        if (data.getKwh() > threshold) {
            alertService.sendAlert();
        }
    }
}
