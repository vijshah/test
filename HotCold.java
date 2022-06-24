import java.io.IOException;
import java.util.List;
import java.util.Random;

import org.apache.zookeeper.CreateMode;
import org.apache.zookeeper.KeeperException;
import org.apache.zookeeper.WatchedEvent;
import org.apache.zookeeper.Watcher;
import org.apache.zookeeper.ZooKeeper;
import org.apache.zookeeper.Watcher.Event.EventType;
import org.apache.zookeeper.data.ACL;
import org.apache.zookeeper.data.Stat;

public class HotCold implements Watcher {
    private ZooKeeper zk;
    private List<ACL> acl;
    private String serverId;

    private void startZk() {
        try {
            // Some unique id for this instance. Could be {Host+Pid} also.
            serverId = Long.toHexString(new Random().nextLong());
            System.out.println("Assigned Unique ID: " + serverId);
            // Zookeeper client and default acl
            zk = new ZooKeeper("localhost:2181", 2000, this);
            Stat stat = new Stat();
            acl = zk.getACL("/", stat);
        } catch (IOException | KeeperException | InterruptedException e) {
            e.printStackTrace();
        }
    }

    private boolean createNode() {
        boolean retval = false;
        try {
            String node = zk.create("/test1/master", serverId.getBytes(), acl, CreateMode.EPHEMERAL);
            System.out.println("Node created " + node);
            retval = true;
        } catch (KeeperException | InterruptedException e) {
            System.out.println("Unable to create node.");
        }
        return retval;
    }

    private boolean isMaster() {
        Stat stat = new Stat();
        String data;
        boolean retVal = false; // assume not a master by default

        // Check if node exists else attempt to create
        try {
            stat = zk.exists("/test1/master", false);
        } catch (KeeperException | InterruptedException e1) {
            System.out.println("Node does not exist.");
        }

        if (null == stat) {
            System.out.println("Node not found trying to create...");
            if (!createNode()) {
                System.out.println("Unable to create node.");
            }
            ;
        }
        try {
            data = new String(zk.getData("/test1/master", this, stat));
            if (data.equals(serverId)) {
                retVal = true;
            }
        } catch (KeeperException | InterruptedException e) {
            assert true; // do nothing
        }
        return retVal;
    }

    private void process() {
        while (true) {
            try {
                if (isMaster()) {
                    System.out.println("Hot: Running Task.");
                    Thread.sleep(3000);
                } else {
                    System.out.println("Cold: Sleeping.");
                    Thread.sleep(3000);
                }
            } catch (InterruptedException e) {
                e.printStackTrace();
            }
        }
    }

    @Override
    public void process(WatchedEvent event) {
        System.out.println("State: " + event.getState() + ", Type: " + event.getType() + ", Path: " + event.getPath());
        if (event.getType() == EventType.NodeDeleted) {
            System.out.println("Trying to create node from event.");
            if (!createNode()) {
                System.out.println("Unable to create node.");
            }
            ;
        }
    }

    public static void main(String[] args) {
        HotCold app = new HotCold();
        app.startZk();
        app.process();
    }
}
