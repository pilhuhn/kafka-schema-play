package org.acme.kafka;

import org.eclipse.microprofile.reactive.messaging.Channel;
import org.eclipse.microprofile.reactive.messaging.Emitter;

import javax.enterprise.context.ApplicationScoped;
import javax.inject.Inject;
import javax.ws.rs.PUT;
import javax.ws.rs.Path;

/**
 * @author hrupp
 */
@ApplicationScoped
@Path("/")
public class KafkaSender {

    @Inject
    @Channel("outChan")
    Emitter emitter;

    @PUT
    public void sendToKafka() {

        emitter.send("Hello World");

    }

}
