package org.acme.kafka;

import org.eclipse.microprofile.reactive.messaging.Incoming;

import javax.enterprise.context.ApplicationScoped;

/**
 * @author hrupp
 */
@ApplicationScoped
public class KafkaReceiver {

//    @Incoming("myChan")
    public void receive(Object o) {
        System.out.println(o);
        System.out.flush();
    }
}
