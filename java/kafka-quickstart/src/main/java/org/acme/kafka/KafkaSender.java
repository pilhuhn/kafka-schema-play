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
    Emitter<Foo> emitter;

    @PUT
    public void sendToKafka() {

        Foo foo = new Foo();
        foo.foo = "Hello Foo";
        foo.bar = 42;

        emitter.send(foo);

    }

    public static class Foo {
        public String foo;
        public int bar;
    }
}
