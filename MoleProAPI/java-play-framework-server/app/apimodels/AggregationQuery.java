package apimodels;

import apimodels.Property;
import java.util.ArrayList;
import java.util.List;
import com.fasterxml.jackson.annotation.*;
import java.util.Set;
import javax.validation.*;
import java.util.Objects;
import javax.validation.constraints.*;
/**
 * AggregationQuery
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaPlayFrameworkCodegen", date = "2020-03-04T17:03:22.330-05:00[America/New_York]")

@SuppressWarnings({"UnusedReturnValue", "WeakerAccess"})
public class AggregationQuery   {
  @JsonProperty("operation")
  private String operation;

  @JsonProperty("controls")
  private List<Property> controls = null;

  @JsonProperty("collection_ids")
  private List<String> collectionIds = new ArrayList<>();

  public AggregationQuery operation(String operation) {
    this.operation = operation;
    return this;
  }

   /**
   * Gene-list aggregation operation, one of 'union', 'intersection', 'difference','symmetric difference'.
   * @return operation
  **/
  @NotNull
  public String getOperation() {
    return operation;
  }

  public void setOperation(String operation) {
    this.operation = operation;
  }

  public AggregationQuery controls(List<Property> controls) {
    this.controls = controls;
    return this;
  }

  public AggregationQuery addControlsItem(Property controlsItem) {
    if (controls == null) {
      controls = new ArrayList<>();
    }
    controls.add(controlsItem);
    return this;
  }

   /**
   * Values that control the behavior of the aggregator. Names of the controls must match the names specified in the aggregator's definition and values must match types (and possibly  allowed_values) specified in the aggregator's definition.
   * @return controls
  **/
  @Valid
  public List<Property> getControls() {
    return controls;
  }

  public void setControls(List<Property> controls) {
    this.controls = controls;
  }

  public AggregationQuery collectionIds(List<String> collectionIds) {
    this.collectionIds = collectionIds;
    return this;
  }

  public AggregationQuery addCollectionIdsItem(String collectionIdsItem) {
    collectionIds.add(collectionIdsItem);
    return this;
  }

   /**
   * Ids of the collections to be aggregated.
   * @return collectionIds
  **/
  @NotNull
  public List<String> getCollectionIds() {
    return collectionIds;
  }

  public void setCollectionIds(List<String> collectionIds) {
    this.collectionIds = collectionIds;
  }


  @Override
  public boolean equals(java.lang.Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    AggregationQuery aggregationQuery = (AggregationQuery) o;
    return Objects.equals(operation, aggregationQuery.operation) &&
        Objects.equals(controls, aggregationQuery.controls) &&
        Objects.equals(collectionIds, aggregationQuery.collectionIds);
  }

  @Override
  public int hashCode() {
    return Objects.hash(operation, controls, collectionIds);
  }

  @SuppressWarnings("StringBufferReplaceableByString")
  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class AggregationQuery {\n");
    
    sb.append("    operation: ").append(toIndentedString(operation)).append("\n");
    sb.append("    controls: ").append(toIndentedString(controls)).append("\n");
    sb.append("    collectionIds: ").append(toIndentedString(collectionIds)).append("\n");
    sb.append("}");
    return sb.toString();
  }

  /**
   * Convert the given object to string with each line indented by 4 spaces
   * (except the first line).
   */
  private String toIndentedString(java.lang.Object o) {
    if (o == null) {
      return "null";
    }
    return o.toString().replace("\n", "\n    ");
  }
}

