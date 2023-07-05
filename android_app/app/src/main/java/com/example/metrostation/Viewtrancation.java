package com.example.metrostation;

import androidx.appcompat.app.AlertDialog;
import androidx.appcompat.app.AppCompatActivity;

import android.content.DialogInterface;
import android.content.Intent;
import android.content.SharedPreferences;
import android.net.Uri;
import android.os.Bundle;
import android.preference.PreferenceManager;
import android.util.Log;
import android.view.View;
import android.widget.AdapterView;
import android.widget.ArrayAdapter;
import android.widget.ListView;
import android.widget.Toast;

import org.json.JSONArray;
import org.json.JSONObject;

public class Viewtrancation extends AppCompatActivity implements JsonResponse, AdapterView.OnItemClickListener {
    ListView l1;
    String[] trid,amount, fromplace, toplace,date,statu,travelstatu,value;
    SharedPreferences sh;

    public static  String lati,longi;
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_viewtrancation);

        sh = PreferenceManager.getDefaultSharedPreferences(getApplicationContext());
        l1 = (ListView) findViewById(R.id.lvview);
        l1.setOnItemClickListener(this);

        JsonReq JR = new JsonReq();
        JR.json_response = (JsonResponse) Viewtrancation.this;
        String q = "/Viewtrancation?lid="+sh.getString("log_id","");
        q = q.replace(" ", "%20");
        JR.execute(q);
    }

    @Override
    public void response(JSONObject jo) {
        try {


            String status = jo.getString("status");
            Log.d("pearl", status);


            if (status.equalsIgnoreCase("success")) {
                JSONArray ja1 = (JSONArray) jo.getJSONArray("data");

                trid= new String[ja1.length()];
                amount = new String[ja1.length()];
                fromplace = new String[ja1.length()];

                toplace = new String[ja1.length()];
                    date = new String[ja1.length()];
                statu = new String[ja1.length()];
                travelstatu = new String[ja1.length()];
                value = new String[ja1.length()];

                for (int i = 0; i < ja1.length(); i++) {

                    trid[i] = ja1.getJSONObject(i).getString("transaction_id");
                    amount[i] = ja1.getJSONObject(i).getString("amount");

                    fromplace[i] = ja1.getJSONObject(i).getString("fromplace");
                    toplace[i] = ja1.getJSONObject(i).getString("toplace");

                    date[i] = ja1.getJSONObject(i).getString("date");

                    statu[i] = ja1.getJSONObject(i).getString("status");
                    travelstatu[i] = ja1.getJSONObject(i).getString("travelstatus");



                    value[i] ="transaction_id:" +trid[i] +"\namount: " + amount[i] + "\nfromplace: " + fromplace[i] + "\ntoplace: " + toplace[i] + "\ndate: " + date[i] + "\nstatus: " + statu[i] + "\ntravelstatus: " + travelstatu[i];

                }
                ArrayAdapter<String> ar = new ArrayAdapter<String>(getApplicationContext(), android.R.layout.simple_list_item_1, value);
                l1.setAdapter(ar);
            }


        } catch (Exception e) {
            // TODO: handle exception
            e.printStackTrace();
            Toast.makeText(getApplicationContext(), e.toString(), Toast.LENGTH_LONG).show();
        }
    }

    @Override
    public void onItemClick(AdapterView<?> adapterView, View view, int i, long l) {

        lati=fromplace[i];
        longi=toplace[i];
        final CharSequence[] items = {"Location","Cancel"};

        AlertDialog.Builder builder = new AlertDialog.Builder(Viewtrancation.this);
        // builder.setTitle("Add Photo!");
        builder.setItems(items, new DialogInterface.OnClickListener() {
            @Override
            public void onClick(DialogInterface dialog, int item) {

                if (items[item].equals("Location")) {


                    //                    startActivity(new Intent(getApplicationContext(),UserHotelRoomBooking.class));
                    String url = "http://www.google.com/maps?saddr=" + LocationService.lati + "" + "," + LocationService.logi + "" + "&&daddr=" + lati + "," + longi;

                    Intent in = new Intent(Intent.ACTION_VIEW, Uri.parse(url));
                    startActivity(in);

                }

                else if (items[item].equals("Cancel")) {
                    dialog.dismiss();
                }

            }

        });
        builder.show();
    }
}