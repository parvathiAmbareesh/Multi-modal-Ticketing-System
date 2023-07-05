package com.example.metrostation;

import android.content.Intent;
import android.content.SharedPreferences;
import android.os.Bundle;
import android.preference.PreferenceManager;
import android.util.Log;
import android.widget.ImageView;
import android.widget.Toast;

import androidx.appcompat.app.AppCompatActivity;

import com.squareup.picasso.Picasso;

import org.json.JSONObject;

public class View_my_qr extends AppCompatActivity implements JsonResponse {
    ImageView im1;
    SharedPreferences sh;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_view_my_qr);

        sh= PreferenceManager.getDefaultSharedPreferences(getApplicationContext());

        im1=(ImageView) findViewById(R.id.imgqr);


//        GeocodingLocation locationAddress = new GeocodingLocation();
//        locationAddress.getAddressFromLocation(nfplace,
//                getApplicationContext(), new View_my_qr().GeocoderHandler());
//
//        locationAddress.getAddressFromLocation(ntplace,
//                getApplicationContext(), new view_my_qr().GeocoderHandler1());
//
//        Toast.makeText(getApplicationContext(), tolatti+" "+tolongi+" "+folatti+" "+folongi, Toast.LENGTH_LONG).show();

        JsonReq JR=new JsonReq();
        JR.json_response=(JsonResponse)View_my_qr.this;
        String q="/View_my_qr?lid="+sh.getString("log_id","");
        q=q.replace(" ","%20");
        JR.execute(q);

    }

    @Override
    public void response(JSONObject jo) {
        try {

            String status=jo.getString("status");
            Log.d("pearl",status);


            if(status.equalsIgnoreCase("success")){

//                ArrayAdapter<String> ar=new ArrayAdapter<String>(getApplicationContext(),android.R.layout.simple_list_item_1,value);
//                l1.setAdapter(ar);
                String qr_code=jo.getString("data");

                String pth = "http://"+sh.getString("ip", "")+"/"+qr_code;
                pth = pth.replace("~", "");
//	       Toast.makeText(context, pth, Toast.LENGTH_LONG).show();

                Log.d("-------------", pth);
                Picasso.with(getApplicationContext())
                        .load(pth)
                        .placeholder(R.drawable.ic_launcher_background)
                        .error(R.drawable.ic_launcher_background).into(im1);

            }


        }

        catch (Exception e) {
            // TODO: handle exception
            e.printStackTrace();
            Toast.makeText(getApplicationContext(), e.toString(), Toast.LENGTH_LONG).show();
        }
    }
    public void onBackPressed()
    {
        // TODO Auto-generated method stub
        super.onBackPressed();
        Intent b=new Intent(getApplicationContext(),Ipsettings.class);
        startActivity(b);
    }
}