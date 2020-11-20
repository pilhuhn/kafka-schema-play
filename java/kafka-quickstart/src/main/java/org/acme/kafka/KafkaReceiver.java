package org.acme.kafka;

import io.smallrye.reactive.messaging.kafka.DeserializationFailureHandler;
import org.apache.kafka.common.header.Headers;
import org.eclipse.microprofile.reactive.messaging.Incoming;

import javax.enterprise.context.ApplicationScoped;
import javax.inject.Named;

/**
 * @author hrupp
 */
@ApplicationScoped
public class KafkaReceiver {

    @Incoming("myChan")
    public void receive(Object o) {
        System.out.println("Receiver, received: " + o);
        System.out.flush();
    }


    /**
     * Failure handler in case deserialization failed.
     *
     * This needs to be a static inner class for it to work.
     * A top level class did not work for me.
     */
    @ApplicationScoped
    @Named("failure-fallback") // Set the name of the failure handler in application.properties
    public static class DeSerFailureHandler implements DeserializationFailureHandler<Object>
    {
        @Override
        public Object handleDeserializationFailure(String topic, boolean isKey, String deserializer, byte[] data, Exception exception, Headers headers) {
            System.out.println("Deserialization failure for topic " + topic + " and deserializer " + deserializer + ": " + exception.getMessage());
            return null;  // TODO: Customise this generated block
        }
    }

}
